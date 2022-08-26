import sys
input = sys.stdin.readline

import heapq
hq = []

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))

    if not hq:
        for i in arr:
            heapq.heappush(hq, i)
    else:
        for i in arr:
            if hq[0] < i:
                heapq.heappush(hq, i)
                heapq.heappop(hq)

print(hq[0])