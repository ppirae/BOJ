a = list(map(int,input().split()))
for i in range(len(a)):
    a[i] = a[i]**2

print(sum(a)%10)
