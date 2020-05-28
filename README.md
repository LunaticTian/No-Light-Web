# No-Light-Web

适用于[圣光](https://github.com/LunaticTian/Python-Reptilian/blob/master/shengguang.py)爬虫，漫画合集等作品站点展示。


# 依赖

Python3 以上

## 模块

* pip install flask


# 功能

* 账号以及权限验证
* 搜索
* 上下页记录
* 自动添加
* 在线删除

# 使用说明

*  收集下载的图集或者漫画等
* 放置于 [\static\HM01\shengguang](\static\HM01\shengguang) 内
* 修改 [app.py](app.py)账号密码——也可不修改  PS:仅限于 **Account** 版
>  #账号密码验证<br>
>  if username == 'test' and password == 'test':
 
* 启动程序
> python3 app.py

## Account 与 Free 说明

### Account

* 带有账户及权限验证，适用于**[信任级别]**的公开分享。

* 适用场景包含VPS的公共分享或局域网分享。

**注意，此版本删除功能虽有权限限制但成功进入网站者均可使用，请知悉：**

**对其内容造成的任何丢失与损害此项目及本人不承担任何责任。**

修改 [one.html](/templates/one.html) 删除**删除功能**部分：

	<h2 id = 'dibu'><a href={{ "/list/"+titile+"/delete" }}  >删除</a></h2>


#### Free

* 不带有任何权限认证，适用于个人PC，局域网分享。
* 适用场景包含个人PC搭建或局域网分享。


## 登录页

![](https://s1.ax1x.com/2020/05/29/tmnKns.png)

## 首页

![](https://s1.ax1x.com/2020/05/29/tmnnXj.png)

## 搜索
![](https://s1.ax1x.com/2020/05/29/tmnmcQ.png)

## 浏览

![](https://s1.ax1x.com/2020/05/29/tmnDN6.png)
