n = int(input())
a = []
b = []
for i in range(n):
    data = input().split()
    a.append(data[0])
    b.append(data[1])

for i in range(n):
    print(int(a[i]) + int(b[i]))
