import sys
import heapq
input = sys.stdin.readline

t = int(input())
arr = []
for i in range(t):
    n = int(input())
    if n == 0:
        if arr == []:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -n)
