# python3 시간초과
# pypy3 정답
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a-1][b-1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

s = int(input())
for i in range(s):
    a, b = map(int, input().rstrip().split())
    if graph[a-1][b-1] == INF and graph[b-1][a-1] == INF:
        print(0)
    elif graph[a-1][b-1] > graph[b-1][a-1]:
        print(1)
    else:
        print(-1)
