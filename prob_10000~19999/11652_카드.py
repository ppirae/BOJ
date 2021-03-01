import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dict = Counter(sorted(arr))
max = 0
for i in dict:
    if dict[i] > max:
        max = dict[i]
        index = i
print(index)
