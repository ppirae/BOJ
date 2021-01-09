n = int(input())
a = []
result = []
for i in range(n):
    a.append(input())

for i in range(n):
    result.append(a[i][0]+a[i][-1])

for i in range(n):
    print(result[i])
