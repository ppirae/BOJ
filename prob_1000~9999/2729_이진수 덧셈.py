import sys
from math import gcd
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(str, input().rstrip().split())
    n = "0b" + n
    m = "0b" + m
    n = int(n, 2)
    m = int(m, 2)
    result = n + m
    print(str(bin(result))[2:])
