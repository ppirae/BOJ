# python3 시간초과
# pypy3 정답

import sys
import math
def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(sys.stdin.readline())
    result = []
    if n == 0:
        break
    else:
        for i in range(n+1, 2*n+1):
            result.append(is_prime(i))
    print(result.count(True))
