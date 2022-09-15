# 구현
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().rstrip().split())))

height = 0
ans = 1e9
for i in range(257):
    MAX = 0
    MIN = 0
    for j in range(n):
        for k in range(m):
            if g[j][k] < i:
                MIN += (i - g[j][k])
            else:
                MAX += (g[j][k] - i)
    block = MAX + b
    if block < MIN:
        continue
    time = 2 * MAX + MIN
    if time <= ans:
        ans = time
        height = i

print(ans, height)