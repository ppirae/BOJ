a, b = map(int, input().split())
arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))

arr3 = arr1 - arr2
print(len(arr3))
arr4 = sorted(list(arr3))
for i in arr4:
    print(i, end = ' ')
