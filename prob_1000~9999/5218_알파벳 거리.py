n = int(input())

for i in range(n):
    result = []
    a, b = map(str,input().split())
    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]):
            result.append(ord(b[i])-ord(a[i]))
        else:
            result.append(26 - (ord(a[i])-ord(b[i])))
    print("Distances: ", end = '')
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()
