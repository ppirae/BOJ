t = int(input())
print("Gnomes:")
for i in range(t):
    arr = list(map(int, input().split()))
    arr2 = sorted(arr)
    arr3 = sorted(arr, reverse=True)
    if arr == arr2 or arr == arr3:
        print("Ordered")
    else:
        print("Unordered")