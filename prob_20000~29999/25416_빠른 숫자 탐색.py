import sys
input = sys.stdin.readline
from collections import deque

dQ = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

g = []
for i in range(5):
    g.append(list(map(int, input().split())))

dis = [[0] * 5 for _ in range(5)]

n, m = map(int, input().split())

c, d = 0, 0
for i in range(5):
    for j in range(5):
        if g[i][j] == 1:
            c = i
            d = j

dQ.append((n, m))
dis[n][m] = 1
g[n][m] = 2
while dQ:
    x, y = dQ.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        if g[nx][ny] == -1:
            continue
        if g[nx][ny] == 0 or g[nx][ny] == 1:
            dis[nx][ny] = dis[x][y] + 1
            g[nx][ny] = 2
            dQ.append((nx, ny))

print(dis[c][d]-1)