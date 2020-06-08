'''
【问题描述】
编写与字符串对象的find方法功能相似的函数find(srcString, substring, start, end)，
作用是在srcString串的下标start到下标end之间的片段中寻找subString串的所有出现。
如果有多处出现，各下标位置用西文逗号','隔开。如果一次都没有出现，则输出"none"。
【输入形式】
按照somestrig,substring,start,end的顺序输入，之间由空格隔开。somestring和subst
ring均由A/T/C/G四个字母组成。start和end由自然数构成。
【输出形式】当匹配成功时，输出子串在DNA字符串的所有位置，以子串第一个字母在DNA字符
串中匹配位置的下标（从0开始），中间用西文逗号","隔开；当匹配失败时，输出"none"。
'''

srcString, subString, start, end =  input().split(" ")
l1 = len(subString)
list1= list(srcString)
list2 = list(subString)
start = int(start)
end = int(end)
temp = 0
array= []
while start <= end:
    if list1[start] == list2[temp]:
        start+=1
        temp+=1
    else:
        start = start - temp + 1
        temp = 0
    if temp == 1:
        array.append(start-end)
        start = start - temp +1
        temp = 0
l2 = len(array)
if l2 == 0:
    print('none')
else:
    for i in range(l2-1):
        print(array[i], end = ',')
    print(array[l2-1])

