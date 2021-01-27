n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))
result = 0
for i in range(len(a)):
    result += a[i] * b[i]
print(result)
