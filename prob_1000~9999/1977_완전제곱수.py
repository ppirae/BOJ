import math
n = int(input())
m = int(input())
result = []
for i in range(n, m+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        result.append(i)

if result != []:
    print(sum(result))
    print(min(result))
else:
    print("-1")
