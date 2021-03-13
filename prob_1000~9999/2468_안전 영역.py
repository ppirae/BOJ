import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n)]
tmp = [[] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().rstrip().split()))

tmp = copy.deepcopy(graph)
num_max = max(map(max, graph))

def dfs(x, y, max):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] > max:
        graph[x][y] = -1
        dfs(x+1 ,y, max)
        dfs(x, y+1, max)
        dfs(x-1, y, max)
        dfs(x, y-1, max)
        return True
    return False

result = 0
for i in range(0, num_max+1):
    cnt = 0
    graph = copy.deepcopy(tmp)
    for j in range(n):
        for k in range(n):
            if dfs(j, k, i) == True:
                cnt += 1
    result = max(result, cnt)
print(result)
