def main():
    n = input()
    n = n.split('-')
    c = ''.join(n)
    tans21SBN13(c)

list1 = [9, 7, 8]
def tans21SBN13(s):
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sun3 = 0
    temp = 0
    for i in s:
        list1.append(i)
    for i in range(1, 13):
        if i % 2 == 0:
            sum1+= int(list1[i-1])*3
        else:
            sum2+= int(list1[i-1])
    sum0 = sum1+sum2
    sun3 = 10 - sum0%10

    if 0 <= sun3 <= 9:
        list1[12] = sun3
    if sun3 == 10:
        list1[12] = 0
    for i in list1:
        temp += 1
        print(i, end='')
        if temp in [3, 4, 7, 12]:
            print("-", end='')

main()