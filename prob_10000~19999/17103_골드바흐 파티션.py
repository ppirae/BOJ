# python3 시간 초과
# pypy3 정답

import sys
import math
input = sys.stdin.readline

prime = [True for i in range(1000001)]
prime[0] = False
prime[1] = False
for i in range(2, 1000001):
    for j in range(i * 2, 1000001, i):
        prime[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    div = n//2
    cnt = 0
    for j in range(2, div+1):
        if prime[n-j] == True and prime[j] == True:
            cnt += 1
    print(cnt)
