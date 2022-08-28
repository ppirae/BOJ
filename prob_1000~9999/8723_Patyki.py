arr = []
arr = list(map(int, input().split()))
arr.sort()
c = arr[2] ** 2
a = arr[0] ** 2
b = arr[1] ** 2
if c == (a+b):
    print(1)
elif arr[0] == arr[1] and arr[2] == arr[0]:
    print(2)
else:
    print(0)