arr = list(map(int, input().split()))
arr.sort(reverse=True)
sum = 0
sum += arr[0] - arr[1]
sum += arr[0] - arr[2]
print(sum)