# python3 시간초과
# pypy3 정답

import math
import sys

def is_prime_number(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def is_rev_prime(x):
    if '3' in x or '4' in x or '7' in x:
        return False

    if is_prime_number(int(x)):
        x = list(x[::-1])
        for i in range(len(x)):
            if x[i] == '6':
                x[i] = '9'
            elif x[i] == '9':
                x[i] = '6'
            else:
                continue
        x = int(''.join(x))
        if is_prime_number(x):
            return True
    return False

n = sys.stdin.readline().rstrip()
if is_rev_prime(n):
    print("yes")
else:
    print("no")
