import sys
input = sys.stdin.readline

def find(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return False


t = int(input())
for i in range(t):
    result = []
    n1 = int(input())
    arr1 = sorted(list(map(int, input().rstrip().split())))

    n2 = int(input())
    arr2 = list(map(int, input().rstrip().split()))

    for j in arr2:
        if find(arr1, j) == True:
            print(1)
        else:
            print(0)
