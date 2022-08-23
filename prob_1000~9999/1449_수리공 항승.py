pipe = [False] * 1001
n, l = map(int, input().split())
for i in map(int, input().split()):
    pipe[i] = True

res = 0
x = 0
while x <= 1000:
    if pipe[x]:
        res += 1
        x += l
    else:
        x += 1

print(res)