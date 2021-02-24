n = int(input())
arr = list(map(int, input().split()))
sum = 0
result = 0

arr.sort()
for i in arr:
    sum += i
    result += sum

print(result)
