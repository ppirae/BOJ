n = int(input())
arr1 = list(map(int, input()))
arr2 = list(map(int, input()))

if n % 2 != 0:
    for i in range(len(arr1)):
        if arr1[i] == 1:
            arr1[i] = 0
        else:
            arr1[i] = 1

if arr1 == arr2:
    print("Deletion succeeded")
else:
    print("Deletion failed")
