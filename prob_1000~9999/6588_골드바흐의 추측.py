import sys
import math
input = sys.stdin.readline

prime = [True for i in range(1000001)]
prime[1] = False
for i in range(2, 1000001):
    for j in range(i * 2, 1000001, i):
        prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = 2
        div = n//2
        for j in range(a, div+1):
            if prime[n-j] == True and prime[j] == True:
                print(n, "=", j, "+", n-j)
                break
