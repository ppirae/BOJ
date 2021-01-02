a = int(input())
b = [0 for i in range(a)]

b = input().split(" ")

for i in range(a):
    b[i] = int(b[i])
b.sort()
for i in range(a):
    b[i] = (b[i] / b[a-1])*100

print(sum(b)/a)
