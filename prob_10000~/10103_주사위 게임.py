n = int(input())
CY = 100
SD = 100
for i in range(n):
    a,b = map(int,input().split())
    if a>b:
        SD -= a
    elif a<b:
        CY -= b
    else:
        continue

print(CY)
print(SD)
