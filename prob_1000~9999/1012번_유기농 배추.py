# python3 런타임 에러
# pypy3 정답 처리

import sys
sys.setrecursionlimit(1500)

t = int(input())

def dfs(graph, i, j):
    if i<0 or i>=n or j<0 or j>=m or graph[i][j] == 0:
        return

    graph[i][j] = 0
    dfs(graph, i+1, j)
    dfs(graph, i-1, j)
    dfs(graph, i, j+1)
    dfs(graph, i, j-1)


for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0]*m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for I in range(len(graph)):
        for J in range(len(graph[0])):
            if graph[I][J] == 1:
                dfs(graph, I, J)
                cnt += 1

    print(cnt)
