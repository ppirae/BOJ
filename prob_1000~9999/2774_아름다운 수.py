import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    arr = [0] * 10
    s = input().rstrip()
    cnt = 0
    for j in s:
        arr[int(j)] += 1
    for k in arr:
        if k != 0:
            cnt += 1

    print(cnt)