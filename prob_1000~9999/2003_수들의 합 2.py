import sys
n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left = 0
cnt = 0
sum = 0
for i in arr:
    sum += i
    if sum >= target:
        while sum >= target:
            if sum == target:
                cnt += 1
            sum -= arr[left]
            left += 1

print(cnt)
