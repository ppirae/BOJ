import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
