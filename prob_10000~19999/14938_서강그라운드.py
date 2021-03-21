import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().rstrip().split())
item = list(map(int, input().rstrip().split()))
graph = [[INF]*n for i in range(n)]

for i in range(r):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = []
for i in range(len(graph)):
    sum = 0
    for j in range(len(graph[i])):
        if graph[i][j] <= m:
            sum += item[j]
    result.append(sum)

print(max(result))
