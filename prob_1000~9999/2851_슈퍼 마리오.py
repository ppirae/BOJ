import sys
input = sys.stdin.readline

arr = []
for i in range(10):
    arr.append(int(input()))

sum = 0
index = 0
for i in range(len(arr)):
    sum += arr[i]
    if sum > 100:
        index = i
        break

before = sum - arr[index]
if abs(sum-100) > abs(before-100):
    print(before)
elif abs(sum-100) < abs(before-100):
    print(sum)
else:
    print(sum)
0))
