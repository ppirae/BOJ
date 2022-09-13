# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

flag = False
visited = [False] * (n+1)

def DFS(now, depth):
    global flag
    if depth == 5:
        flag = True
        return
    visited[now] = True
    for i in g[now]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[now] = False

for i in range(n):
    DFS(i, 1)
    if flag:
        break

print(1 if flag else 0)