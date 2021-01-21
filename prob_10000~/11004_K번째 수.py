import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = n-1
target = k
arr.sort()
print(arr[k-1])
