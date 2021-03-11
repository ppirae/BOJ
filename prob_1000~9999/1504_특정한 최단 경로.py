import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().rstrip().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

v1, v2 = map(int, input().rstrip().split())

road_one = dijkstra(1)
road_v1 = dijkstra(v1)
road_v2 = dijkstra(v2)
result = min(road_one[v1] + road_v1[v2] + road_v2[n], road_one[v2] + road_v2[v1] + road_v1[n])
print(result if result < INF else -1)
