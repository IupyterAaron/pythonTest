'''
【问题描述】

        凯撒密码是古罗马凯撒大帝用来保护重要军情的加密系统。这套密码系统在现在看来很低级，但是在古罗马时期还是发挥了重要作用的。
        凯撒密码的根本思想是按照字母表排列顺序将明文中每个字母变换成其后第n个字母。这里，n（n=1~25）被称作秘钥。
        请编写程序，针对不同的输入字符串和移动位数，输出经过凯撒加密之后的字符串。
【输入形式】
第一个输入参数是移动的位数n，中间间隔一个空格之后，第二个输入参数是待加密的原文字符串
【输出形式】
加密后的密文字符串。注意，只加密字母，且不改变字母大小写。待加密的字符串可能存在比如"hello world"的形式，若与第一个参数一起以input的方式输入，在调用split()的时候要注意，会将待加密字符串也一并分割了。split()方法有参数指定分割多少项，建议采用，请上网搜索说明文档。
【样例输入】
5 NUDT
【样例输出】
SZIY
'''

str = input()
k, s = str.split(' ', 1)
k = int(k)
s_list = list(s[:])
s_new_list = []

for i in s_list:
    if i.isalpha():
        if (ord(i)>= 97 and 123-k > ord(i)) or (ord(i)>=65 and 91-k>ord(i)):
            s_new_list.append(chr(ord(i)+k))
        else:
            s_new_list.append(chr(ord(i)-(26-k)))
    else:
        s_new_list.append(i)
w = "".join(s_new_list)
print(w)