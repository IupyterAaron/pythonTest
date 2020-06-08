def upper(s):
    list1= []
    for i in s:
        list1.append(i)
    for i in list1:
        if 97 <= ord(i) <= 122:
            num = ord(i)-32
            print(chr(num), end = '')
        else:
            print(i, end = '')