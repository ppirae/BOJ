import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(str, input().strip())) for _ in range(n)]
cnt = []

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (l + k) % 2 == 0:
                    if g[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if g[k][l] != 'B':
                        w += 1
                    else:
                        b += 1
        cnt.append(w)
        cnt.append(b)

print(min(cnt))