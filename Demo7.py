s = int(input())

for i in range(1, s+1, 2):
    p = int((s-i)/2)
    for j in range(p):
        print(" ",end="")
    for k in range(i):
        print("*", end = "")
    print()
