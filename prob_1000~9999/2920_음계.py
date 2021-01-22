arr = list(map(int, input().split()))
ac = sorted(arr)
dc = sorted(arr, reverse=True)
if arr == ac:
    print("ascending")
elif arr == dc:
    print("descending")
else:
    print("mixed")
