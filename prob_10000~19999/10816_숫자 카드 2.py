import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

d = defaultdict(int)
for i in arr:
    d[i] += 1

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in d.keys():
        print(d.get(i), end = ' ')
    else:
        print(0, end = ' ')