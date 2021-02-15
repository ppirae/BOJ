import sys
from collections import Counter
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(int(sys.stdin.readline()))

arr.sort()

def counter(arr):
    counter_dict = Counter(arr)
    counter_arr = [i for i, j in counter_dict.items() if j == max(counter_dict.values())]
    counter_arr.sort()

    if len(counter_arr) == 1:
        return counter_arr[0]
    else:
        return counter_arr[1]

print(round(sum(arr)/t))
print(arr[t//2])
print(counter(arr))
print(max(arr) - min(arr))
