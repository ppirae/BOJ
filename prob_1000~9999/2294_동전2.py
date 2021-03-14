import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

d = [10001] * (k+1)
d[0] = 0
for i in range(n):
    for j in range(coin_types[i], k+1):
        d[j] = min(d[j], d[j- coin_types[i]]+1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])
