import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] += arr[i-1] if arr[i-1] > 0 else 0

print(max(arr))
