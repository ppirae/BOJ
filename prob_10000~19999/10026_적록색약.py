import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

n = int(input())
graph = [[0] for i in range(n)]

for i in range(n):
    graph[i] = list(map(str, input().rstrip()))

def dfs_R(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 'R':
        return

    graph[i][j] = 'r'
    dfs_R(graph, i+1, j)
    dfs_R(graph, i-1, j)
    dfs_R(graph, i, j+1)
    dfs_R(graph, i, j-1)

def dfs_G(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 'G':
        return

    graph[i][j] = 'r'
    dfs_G(graph, i+1, j)
    dfs_G(graph, i-1, j)
    dfs_G(graph, i, j+1)
    dfs_G(graph, i, j-1)

def dfs_B(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 'B':
        return

    graph[i][j] = 'b'
    dfs_B(graph, i+1, j)
    dfs_B(graph, i-1, j)
    dfs_B(graph, i, j+1)
    dfs_B(graph, i, j-1)

def dfs_r(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 'r':
        return

    graph[i][j] = '0'
    dfs_r(graph, i+1, j)
    dfs_r(graph, i-1, j)
    dfs_r(graph, i, j+1)
    dfs_r(graph, i, j-1)

def dfs_b(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 'b':
        return

    graph[i][j] = '0'
    dfs_b(graph, i+1, j)
    dfs_b(graph, i-1, j)
    dfs_b(graph, i, j+1)
    dfs_b(graph, i, j-1)

count_normal = 0
count_RG = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            dfs_R(graph, i, j)
            count_normal += 1
        if graph[i][j] == 'G':
            dfs_G(graph, i, j)
            count_normal += 1
        if graph[i][j] == 'B':
            dfs_B(graph, i, j)
            count_normal += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'r':
            dfs_r(graph, i, j)
            count_RG += 1
        if graph[i][j] == 'b':
            dfs_b(graph, i, j)
            count_RG += 1

print(count_normal, count_RG)
