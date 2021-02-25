# python3 시간 초과
# pypy3 정답

import sys
input = sys.stdin.readline

def fibo(n, q):
    d = [0] * 10001
    d[1] = 1 % q
    d[2] = 1 % q
    d[3] = 2 % q
    for i in range(4, n+1):
        d[i] = (d[i-1] + d[i-2]) % q

    return d[n]

t = int(input())
for i in range(t):
    p, q = map(int, input().split())
    print("Case #" + str(i+1) + ": " + str(fibo(p, q)))
