import sys
input = sys.stdin.readline

max = 100000
d = [0] * (max+1)
d[1] = 1
d[2] = 1
for i in range(3, max+1):
    d[i] = d[i-1] + d[i-2]

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(mid)
            break
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False

t = int(input())
for i in range(t):
    n = int(input())
    binary_search(d, n)
