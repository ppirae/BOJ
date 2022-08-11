n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if arr.index(i)+1 != i:
        cnt += 1

print(cnt)