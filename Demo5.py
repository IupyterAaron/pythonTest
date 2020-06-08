'''
【样例输入】Mike
【样例输出】

print "Happy Birthday to you!"
print "Happy Birthday to you!"
print "Happy Birthday，dear Mike!"
print "Happy Birthday to you!"
'''
'''
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
'''
name = input()
site = {"name":name}
print("Happy birthday to you!")
print("Happy birthday to you!")
print("Happy birthday, dear {name}!".format(**site))
print("Happy birthday to you!")