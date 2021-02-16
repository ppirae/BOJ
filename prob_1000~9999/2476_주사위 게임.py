t = int(input())
result = []
price = 0
for i in range(t):
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] and arr[1] == arr[2]:
        price = 10000 + arr[0] * 1000
        result.append(price)
    elif arr[0] == arr[1] and arr[1] != arr[2]:
        price = 1000 + arr[0] * 100
        result.append(price)
    elif arr[1] == arr[2] and arr[0] != arr[2]:
        price = 1000 + arr[1] * 100
        result.append(price)
    elif arr[0] == arr[2] and arr[0] != arr[1]:
        price = 1000 + arr[2] * 100
        result.append(price)
    else:
        price = max(arr) * 100
        result.append(price)
print(max(result))
