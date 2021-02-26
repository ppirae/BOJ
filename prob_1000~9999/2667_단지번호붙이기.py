import sys
sys.setrecursionlimit(1500)
input = sys.stdin.readline

n = int(input())
graph = [[0] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().rstrip()))

def dfs(graph, i, j, num):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] != 1:
        return

    graph[i][j] = num
    dfs(graph, i+1, j, num)
    dfs(graph, i-1, j, num)
    dfs(graph, i, j+1, num)
    dfs(graph, i, j-1, num)

count = 0
num = 101
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(graph, i, j, num)
            count += 1
            num += 1

cnt = 0
for i in range(count):
    for j in range(n):
        for k in range(n):
            if graph[j][k] == (101+i):
                cnt += 1
    result.append(cnt)
    cnt = 0

print(count)
result.sort()
for i in result:
    print(i)
