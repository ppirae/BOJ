m, n = map(int,input().split())
k = 0
min = 0
max = 0

if m>n: k = m
else: k = n
for i in range(1,k+1):
    if m%i == 0 and n%i == 0:
        min = i
max = (m//min)*(n//min)*min
print(min)
print(max)
