n = input()
n_max = int(n)
# 先生成一个矩阵
new_a = []
old_a = []

for i in range(2 * n_max - 1) :
    for j in range(2 * n_max  - 1) :
        new_a.append(0)
    old_a.append(new_a)
    new_a = []

num = 1

for i in range(n_max) :
    for j in range(i, n_max * 2 - (1 + i)) :
        old_a[j][i] = old_a[i][j] = old_a[j][2 * n_max - 2 - i] = old_a[2 * n_max - 2 - i][j] = num
    num+=1

for i in old_a :
    for j in i :
        print(j, end="")
    print()
