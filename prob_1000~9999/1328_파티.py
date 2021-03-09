import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, end = map(int, input().rstrip().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start_end = []
end_start = []
result = [0 for i in range(n)]
for i in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(i)
    start_end.append(distance[end])

distance = [INF] * (n+1)
for i in range(1, n+1):
    dijkstra(end)
    end_start.append(distance[i])

for i in range(n):
    result[i] = start_end[i] + end_start[i]

print(max(result))
