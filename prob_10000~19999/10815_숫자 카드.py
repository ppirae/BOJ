import sys
input = sys.stdin.readline

n = int(input())
arr1 = sorted(list(map(int, input().rstrip().split())))

m = int(input())
arr2 = list(map(int, input().rstrip().split()))

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False

result = []
for i in arr2:
    result.append(binary_search(arr1, i))

for i in result:
    if i == True:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
