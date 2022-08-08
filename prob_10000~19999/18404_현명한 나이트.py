import sys
input = sys.stdin.readline

from collections import deque

dQ = deque()
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

n, m = map(int, input().split())
def reset_board():
    board = [[0 for _ in range(n)] for _ in range(n)]
    return board

ch = reset_board()
a, b = map(int, input().split())
dQ.append((a-1, b-1))
ch[a-1][b-1] = 1
while dQ:
    x, y = dQ.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if ch[nx][ny] == 0:
            ch[nx][ny] = ch[x][y] + 1
            dQ.append((nx, ny))

result = []
for i in range(m):
    c, d = map(int, input().split())
    result.append(ch[c-1][d-1]-1)

for i in result:
    print(i, end = ' ')