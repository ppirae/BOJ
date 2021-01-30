n, m = map(int,input().split())
arr1 = []
arr2 = []
result = [[] for i in range(n)]
for i in range(n):
    arr1.append(list(map(int,input().split())))
for i in range(n):
    arr2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        result[i].append(arr1[i][j] + arr2[i][j])

for i in range(n):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')
    print()
