import sys
import math
input = sys.stdin.readline

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x == 0 or x == 1:
            return False
        if x % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print(2)
    elif n == 1:
        print(2)
    else:
        while True:
            if is_prime(n):
                print(n)
                break
            else:
                n += 1
