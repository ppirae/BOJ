n = int(input())
mirror = [[] for _ in range(n)]
for i in range(n):
    mirror[i] = list(map(str,input()))
k = int(input())

if k == 1:
    for i in range(n):
        for j in range(n):
            print(mirror[i][j], end ='')
        print()
elif k == 2:
    for i in range(n):
        mirror[i].reverse()

    for i in range(n):
        for j in range(n):
            print(mirror[i][j], end ='')
        print()
else:
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(mirror[i][j], end ='')
        print()
