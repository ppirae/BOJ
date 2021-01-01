n = int(input())
l = list(map(int,input().split(" ")))
sum = 0
result = 0

l.sort()
for i in range(n):
    sum += l[i]
    result += sum

print(result)
