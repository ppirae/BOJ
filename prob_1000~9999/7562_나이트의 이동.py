import sys
input = sys.stdin.readline

from collections import deque

dq = deque()
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

t = int(input())
for i in range(t):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    a, b = map(int,input().split())
    c, d = map(int,input().split())
    if a == c and b == d:
        print(0)
    else:
        dq.append((a, b))
        board[a][b] = 1
        while dq:
            x, y = dq.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[nx][ny] == 1:
                    continue
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    dq.append((nx, ny))
                if board[c][d] == 1:
                    break
        print(board[c][d]-1)