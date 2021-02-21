arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
a, b = 0, 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            a = arr[i]
            b = arr[j]

for i in arr:
    if i != a and i != b:
        print(i)
