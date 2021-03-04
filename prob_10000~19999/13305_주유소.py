import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_v = sys.maxsize
total = 0
for i in range(n-1):
    if i == 0:
        total += (price[0] * distance[0])
        min_v = min(min_v, price[i])
    else:
        min_v = min(min_v, price[i])
        total += (min_v * distance[i])

print(total)
