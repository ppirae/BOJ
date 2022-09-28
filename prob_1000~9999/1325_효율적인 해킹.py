import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
A = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    A[a-1].append(b-1)

answer = [0] * n

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now_v = q.popleft()
        for i in A[now_v]:
            if visited[i] == False:
                visited[i] = True
                answer[i] += 1
                q.append(i)

for i in range(n):
    visited = [False] * n
    BFS(i)

MAX = max(answer)

for i in range(len(answer)):
    if answer[i] == MAX:
        print(i+1, end = ' ')