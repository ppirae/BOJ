n = int(input())
sum = 5
nt = 7
for i in range(1, n):
    sum += nt
    nt += 3
print(sum%45678)