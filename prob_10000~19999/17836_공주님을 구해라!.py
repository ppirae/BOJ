import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, t = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

dis = [[0] * m for _ in range(n)]
q = deque()
res = 0

def bfs():
    q.append((0, 0))
    dis[0][0] = 1
    gram = 9999999
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return min(dis[x][y]-1, gram)
        if g[x][y] == 2:
            gram = dis[x][y]-1 + (n-1-x) + (m-1-y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not dis[nx][ny]:
                if g[nx][ny] == 0 or g[nx][ny] == 2:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx, ny))
    return gram

res = bfs()
if res > t:
    print('Fail')
else:
    print(res)