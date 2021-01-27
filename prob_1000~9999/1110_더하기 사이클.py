n = int(input())
res = n
tmp, cnt = 0, 0

while True:
    tmp = res // 10 + res % 10
    res = res % 10 * 10 + tmp % 10
    cnt += 1
    if res == n:
        break

print(cnt)
