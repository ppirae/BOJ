import sys
n = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
target = int(input())
left, right = 0, n-1
cnt = 0
while left < right:
    if arr[left] + arr[right] > target:
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        cnt += 1
        left += 1

print(cnt)
