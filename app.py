import os,random
import shutil

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lunaticsmg'

path = "static/HM01/shengguang"
# 登录界面

nums = []
userEndRead = {}
sum = 0

@app.route('/')
def index_login():
    return render_template("login.html")


def getMl(username, urlwz=None):
    if userEndRead == {} or username not in userEndRead.keys():
        return '/index',"", ""
    return '/list/'+userEndRead[username]['ml'],userEndRead[username]['ml'],userEndRead[username]['wz']



# 详细列表
@app.route('/search',methods=['POST'])
def search():
    global nums, sum
    searchList = []
    keyword = request.form['keyword']

    for i in nums:
        if keyword in i:
            searchList.append(i)
    urlwz, ml, wz = getMl(session['username'])
    sum = sum + 1
    return render_template('search.html', nums=searchList, titile="目录首页", urlwz=urlwz, ml=ml, wz=wz)


# 访问的目录
@app.route('/index')
def index():
    global nums,sum
    if sum == 0 :
        nums = os.listdir(path)
    random.shuffle(nums)
    urlwz ,ml,wz = getMl(session['username'])
    sum = sum + 1
    return render_template('index.html',nums=nums,titile="目录首页",urlwz=urlwz,ml=ml,wz=wz)





# 详细列表
@app.route('/list/<name>')
@app.route('/list')
def one(name):
    nums1 = os.listdir(path+"/"+name)
    intx = nums.index(name)
    try:
        next = "/list/"+nums[intx+1]
    except:
        next = "/list/" + nums[intx]
    if intx == 0:
        last = "/list/"+name
    else:
        last = "/list/"+nums[intx-1]

    urlwz, ml, wz = getMl(session['username'])
    listimg = []
    for  i in nums1:
        i = "HM01/shengguang"+"/"+name+"/"+i
        listimg.append(i)
    return render_template('one.html',nums=listimg,titile=name,urlwz=urlwz,ml=ml,wz=wz,next=next,last=last)

@app.route('/list/<name>/delete')
def delete(name):
    shutil.rmtree(path+"/"+name)
    return redirect(url_for('one', name=random.choice(nums)))



# 验证是否登录
@app.before_request
def before_user():
    if request.path == "/login" or request.path == "/":
        if 'username' in session :
            return redirect(url_for('index'))
        return
    if 'username' not in session and  '/static/' not in request.path:
        return render_template("login.html")
    # 加入阅读位置提醒
    if 'pdf' in request.path:
        userEndRead[session['username']]={'ml':request.path.split('/')[3],'wz':request.path.split('/')[4]}
    return


@app.errorhandler(404)  # 使用app.errorhandler装饰器，传入错误码404
def page_not_found(e):
    return render_template("index.html")  # 返回响应文档404.html，状态码404.(下同）


@app.errorhandler(500)
def internal_server_error(e):
    # return render_template('500.html'), 500
    return render_template("index.html")


# 增加登录用户的session
@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.values.get('username');
        password = request.values.get('password');
        if username == 'lunatic' and password == '494296145':
            session['username'] = username
            print("ok")
            return 'index.html'
        else:
            print("no")
            return "error"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
