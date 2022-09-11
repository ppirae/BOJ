import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr)-1
SUM = 0
cnt = 0

while start < end:
    SUM = arr[start] + arr[end]
    if SUM == m:
        cnt += 1
        start += 1
        end -= 1
    elif SUM > m:
        end -= 1
    else:
        start += 1

print(cnt)