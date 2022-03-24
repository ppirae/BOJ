k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))

def Count(len):
    cnt = 0
    for x in a:
        cnt += x//len
    return cnt

lt = 1
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) < n:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1

print(res)