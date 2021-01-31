import sys
N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start+end)//2
    total = sum([i-mid if mid < i else 0 for i in arr])

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
