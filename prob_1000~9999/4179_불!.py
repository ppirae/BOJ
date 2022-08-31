import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(list(input())[:-1])

disF = [[999] * c for _ in range(r)]
disJ = [[0] * c for _ in range(r)]
dQF = deque()
dQJ = deque()

for i in range(r):
    for j in range(c):
        if g[i][j] == "J":
            dQJ.append((i, j))
            disJ[i][j] = 1
        if g[i][j] == "F":
            dQF.append((i, j))
            disF[i][j] = 1

#불 BFS
while dQF:
    x, y = dQF.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if disF[nx][ny] == 999 and g[nx][ny] != "#":
                disF[nx][ny] = disF[x][y] + 1
                dQF.append((nx, ny))

flag = 0
a_x, a_y = 0, 0
#지훈 BFS
while dQJ:
    x, y = dQJ.popleft()
    if x == r-1 or y == c-1 or x == 0 or y == 0:
        a_x = x
        a_y = y
        flag = 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if disJ[nx][ny] or g[nx][ny] == "#":
            continue
        if disF[nx][ny] <= disJ[x][y] + 1:
            continue
        disJ[nx][ny] = disJ[x][y] + 1
        dQJ.append((nx, ny))

print("IMPOSSIBLE" if flag == 0 else disJ[a_x][a_y])