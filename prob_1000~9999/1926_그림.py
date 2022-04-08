import sys
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
sys.setrecursionlimit(10**6)
res = []
size = 0

def dfs(x, y):
    global size
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        size += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res.append(size)
            size = 0

if len(res) == 0:
    print(len(res))
    print(0)
else:
    print(len(res))
    print(max(res))