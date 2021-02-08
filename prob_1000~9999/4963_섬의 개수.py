# python3 제출 시 런타임에러
# pypy3 제출 시 정답 처리

import sys
sys.setrecursionlimit(1500)

def dfs(graph, i, j):
    if i >= len(graph) or i < 0 or j >= len(graph[0]) or j < 0 or graph[i][j] != 1:
        return

    graph[i][j] = 0
    dfs(graph, i+1, j)
    dfs(graph, i-1, j)
    dfs(graph, i, j-1)
    dfs(graph, i, j+1)
    dfs(graph, i-1, j-1)
    dfs(graph, i-1, j+1)
    dfs(graph, i+1, j+1)
    dfs(graph, i+1, j-1)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        graph = []
        count = 0
        for i in range(m):
            graph.append(list(map(int,input().split())))
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    dfs(graph, i, j)
                    count += 1
        print(count)
