a,b = map(int,input().split())
c = a*b

d = list(map(int,input().split()))
for i in range(5):
    d[i] = d[i] - c

for i in range(5):
    print(d[i],end=" ")
