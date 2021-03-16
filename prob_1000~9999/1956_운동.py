import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in range(len(graph)):
    result.append(graph[i][i])

print(min(result) if min(result) != INF else -1)
