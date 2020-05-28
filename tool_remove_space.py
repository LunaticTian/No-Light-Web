import os
path = "./static/HM01/shengguang/"
nums = os.listdir(path)
print(nums)
for i in nums:
    os.rename(path + i,path + i.replace(" ","-"))