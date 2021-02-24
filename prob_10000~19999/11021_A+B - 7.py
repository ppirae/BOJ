n = int(input())
a = []
b = []
for i in range(n):
    data = input().split()
    a.append(data[0])
    b.append(data[1])

for i in range(n):
    print("Case #"+str(i+1)+":",int(a[i]) + int(b[i]))
