import math
n = int(input())
m = int(input())

result = []

def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in range(n, m+1):
    if is_prime_number(i):
        result.append(i)

if result != []:
    print(sum(result))
    print(min(result))
else:
    print("-1")
