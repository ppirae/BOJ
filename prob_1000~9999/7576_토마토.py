from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*m for _ in range(n)]
Q = deque()
cnt = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            Q.append((i, j))
            ch[i][j] = 0

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and ch[nx][ny]==0 and graph[nx][ny]==0:
            graph[nx][ny] = 1
            ch[nx][ny] = ch[x][y] + 1
            Q.append((nx, ny))

maxx = -2147000000
for i in range(n):
    for j in range(m):
        if ch[i][j] > maxx:
            maxx = ch[i][j]

def is_ok(graph):
    global n, m
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

if is_ok(graph):
    print(maxx)
else:
    print(-1)