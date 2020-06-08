'''
【问题描述】
编写程序，输入十进制小数（只考虑正数），把它转换为以字符串形式存储的二进制小数，输出该二进制小数字符串。对于转换得到的二进制小数，小数点后最多保留10位。小数点后不足10位，则输出这些位，尾部不补0；小数点后超出10位，则直接舍弃超出部分。
【输入形式】
十进制浮点小数
【输出形式】
对应输入小数的二进制小数字符串。若整数部分或者小数部分为0，则输出0。比如输入0，则意味着输出0.0  。
【样例输入】
1.2
【样例输出】
1.0011001100
【样例说明】
输入为10进制小数，将该小数转化成二进制后输出。推荐采用字符串来处理生成的二进制数，特别要注意0的处理
'''
a = float(input())
#print(a)
# 先处理整数
if a == 0.0:
    print('0.0')
else:
    int_a = int(a)
    flo_a = a-int_a
    endshu = 0.00000000
    zhengshu = str(bin(int_a))
    zhengshu = zhengshu[2:]

    xiaoshu = flo_a
    xiaoshus = []

    for i in range(8):
        xiaoshu *= 2
        xiaoshus += str(int(xiaoshu))
        xiaoshu-=int(xiaoshu)
    floend = xiaoshus
    print(zhengshu,"."+''.join(floend)+'00')
