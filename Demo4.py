def findMAx(a,b):
    if a>b:
        return a
    else:
        return b
a, b = input().split(" ")
a = int(a)
b = int(b)
c = 0
c = findMAx(a, b)
print(c)
