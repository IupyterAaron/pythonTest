'''
【问题描述】
输入一个列表，包含若干个整数（允许为空），然后将其中的奇数和偶数单独放置在一个列表中，保持原有顺序
【输入形式】
【输出形式】
分两行输出，第一行输出偶数序列，第二行输出奇数序列
【样例输入1】
[48,82,47,54,55,57,27,73,86,14]
【样例输出1】
48, 82, 54, 86, 14
47, 55, 57, 27, 73
【样例输入2】
[10, 22, 40]
样例输出2】
10, 22, 40
NONE
【样例说明】如果奇偶拆分后，奇数列表，或者偶数列表为空，请直接输出NONE表示
'''
list = input().strip('[]')
jishu = []
oushu = []
list_new = list.split(',')
a = len(list_new)
if a != 0:
    for i in list_new:
        x = int(i)
        if x%2 == 0:
           oushu.append(x)
        else:
           jishu.append(x)
if len(oushu) == 0:
    print('NONE')
else:
    for i in range(len(oushu)):
        if i == len(oushu) - 1:
            print(oushu[i])
        else:
            print(oushu[i], end=', ')
if len(jishu) == 0:
    print("NONE")
else:
    for i in range(len(jishu)):
        if i == len(jishu) - 1:
            print(jishu[i])
        else:
            print(jishu[i], end=', ')
