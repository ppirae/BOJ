import sys
input = sys.stdin.readline

from collections import deque

dQ = deque()
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
ch = [[0 for _ in range(n)] for _ in range(n)]
a, b, c, d = map(int, input().split())

dQ.append((a, b))
ch[a][b] = 1
while dQ:
    x, y = dQ.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if ch[nx][ny] == 0:
            ch[nx][ny] = ch[x][y] + 1
            dQ.append((nx, ny))
        if ch[c][d] == 1:
            break
print(ch[c][d]-1 if ch[c][d] != 0 else -1)