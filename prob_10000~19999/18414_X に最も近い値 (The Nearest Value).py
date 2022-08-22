a, b, c = map(int, input().split())
min = 100001
res = 0
for i in range(b, c+1):
    cha = abs(i - a)
    if cha < min:
        min = cha
        res = i

print(res)