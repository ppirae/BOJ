import sys
input = sys.stdin.readline

arr = [[0 for j in range(15)] for i in range(15)]

for i in range(1, 15):
    arr[i][1] = 1
    arr[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(arr[k][n])