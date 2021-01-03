a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
c = [0 for i in range(len(a))]

for i in range(len(a)):
    c[i] = b[i] - a[i]

for i in range(len(a)):
    print(c[i],end=" ")
