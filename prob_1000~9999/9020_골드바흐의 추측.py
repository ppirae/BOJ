import sys
import math
input = sys.stdin.readline

prime = [True for i in range(10001)]
prime[1] = False
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    div = n//2
    for j in range(div, 1, -1):
        if prime[n-j] == True and prime[j] == True:
            print(j, n-j)
            break
