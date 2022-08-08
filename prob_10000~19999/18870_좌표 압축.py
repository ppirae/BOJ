import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(set(arr))

d = {i:v for v,i in enumerate(arr2)}
for i in arr:
    print(d[i], end = ' ')