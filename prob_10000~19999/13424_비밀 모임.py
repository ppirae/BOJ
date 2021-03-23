import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    graph = [[INF] * n for i in range(n)]
    for _ in range(m):
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
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    k = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = []
    for i in range(len(graph)):
        sum = 0
        for j in arr:
            sum += graph[i][j-1]
        result.append(sum)

    print(result.index(min(result))+1)
