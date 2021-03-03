import sys
import math
input = sys.stdin.readline

max = 1299709
prime = [True] * (max+1)
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(max)+1)):
    if prime[i] == True:
        j = 2
        while i*j <= max:
            prime[i*j] = False
            j += 1

t = int(input())
for i in range(t):
    n = int(input())
    a, b = 0, 0
    if prime[n] == True:
        print(0)
    elif n == 1:
        print(0)
    else:
        for j in range(n-1, 3, -1):
            if prime[j] == True:
                a = j
                break
        for k in range(n+1, max+1):
            if prime[k] == True:
                b = k
                break
        print(b-a)
