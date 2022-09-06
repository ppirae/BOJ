n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)
res = 10**9

while left <= right:
    mid = (left+right)//2
    cnt = 0
    sum = 0
    for i in range(len(arr)):
        if sum + arr[i] > mid:
            cnt += 1
            sum = 0
        sum += arr[i]
    if sum:
        cnt += 1

    if cnt > m:
        left = mid + 1
    else:
        res = min(res, mid)
        right = mid - 1

print(res)