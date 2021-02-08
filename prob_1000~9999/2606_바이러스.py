n = int(input())
m = int(input())
com = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    com[a-1].append(b)
    com[b-1].append(a)

def dfs(graph, v, visited):
    visited[v-1] = True
    for i in graph[v-1]:
        if not visited[i-1]:
            dfs(graph, i, visited)

visited = [False] * n
cnt = 0
dfs(com, 1, visited)

print(visited.count(True)-1)
