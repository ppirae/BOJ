import math
import sys
n, m = map(int, sys.stdin.readline().split())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

for i in range(n, m+1):
    if i == 1:
        continue
    if is_prime_number(i):
        print(i,end = '\n')
