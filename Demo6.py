n, m, p= map(int, input().split())
list = []
for i in range(1,n+1):
    list.append(i)
while True:
    k = (m+p - 1 ) % (len(list))
    if k == 0:
        k = k+len(list)
    p = k
    if len(list) == 1 :
        print(list[k-1], end="")
        break
    else:
        del list[k-1]
