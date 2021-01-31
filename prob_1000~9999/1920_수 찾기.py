import sys
n = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
result = []

def is_in(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in arr2:
    result.append(is_in(arr1, i, 0, len(arr1)-1))

for i in result:
    if i == True:
        print(1)
    else:
        print(0)
