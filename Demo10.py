str = input()
list = []
for i in str:
    list.append(i)
for i in list:
    if 'a'<=i<='z':
        print(i.upper(),end="")
    elif 'A'<=i<='Z':
        print(i.lower(),end="")
    else:
        print(i,end="")