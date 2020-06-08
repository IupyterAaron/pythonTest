a1, b1, c1 = input().split('.')
a2, b2, c2 = input().split('.')

a1_int = int(a1)
a2_int = int(a2)
b1_int = int(b1)
b2_int = int(b2)
c1_int = int(c1)
c2_int = int(c2)

res = 0

if b1_int < b2_int :
    res = a2_int -a1_int
else:
    if b2_int < b1_int:
        res = a2_int-a1_int - 1
    else:
        if c1_int<=c2_int:
            res = a2_int - a1_int
        else:
            res = a2_int - a1_int - 1

print(res)