str = input()

for i in str:
    if 'a'<= i <= 'z':
        n = chr(ord('z')-(ord(i)-ord('a')))
    elif 'A' <= i <= 'Z':
        n = chr(ord('Z') - (ord(i) - ord('A')))
    else:
        n = i
    print(n, end='')