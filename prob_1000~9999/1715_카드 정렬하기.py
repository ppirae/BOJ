# 그리디
import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

heapq.heapify(arr)
ans = 0

while len(arr) > 1:
    temp1 = heapq.heappop(arr)
    temp2 = heapq.heappop(arr)
    temp3 = temp1 + temp2
    ans += temp3
    heapq.heappush(arr, temp3)

print(ans)