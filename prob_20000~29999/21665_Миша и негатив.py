n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input())))

arr2 = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "W":
            arr2[i][j] = "B"
        else:
            arr2[i][j] = "W"

space = input()

arr3 = []
for i in range(n):
    arr3.append(list(map(str, input())))

cnt = 0
for i in range(n):
    for j in range(m):
        if arr2[i][j] != arr3[i][j]:
            cnt += 1

print(cnt)