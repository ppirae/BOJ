import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x: (x[1], x[0]))
start = arr[0][0]
end = arr[0][1]
cnt = 1
for i in range(1, len(arr)):
    if arr[i][0] >= end:
        start = arr[i][0]
        end = arr[i][1]
        cnt += 1

print(cnt)
