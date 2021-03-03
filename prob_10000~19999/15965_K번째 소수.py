import sys
import math
input = sys.stdin.readline

n = 7400000
prime = [True] * (n+1)
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if prime[i] == True:
        j = 2
        while i*j <= n:
            prime[i*j] = False
            j += 1

result = []
for i in range(len(prime)):
    if i != 0 and prime[i] == True:
        result.append(i)

k = int(input())
print(result[k-1])
