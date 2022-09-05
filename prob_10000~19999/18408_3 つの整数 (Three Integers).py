arr = list(map(int, input().split()))
cnt = [0] * 3
for i in arr:
    if i == 1:
        cnt[1] += 1
    else:
        cnt[2] += 1
print(1 if cnt[1] > cnt[2] else 2)