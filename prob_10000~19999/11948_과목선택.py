arr = []
arr2 = []
for _ in range(4):
    arr.append(int(input()))
for _ in range(2):
    arr2.append(int(input()))
arr.sort(reverse=True)
arr2.sort(reverse=True)
print(((sum(arr) - arr[3]) + arr2[0]))