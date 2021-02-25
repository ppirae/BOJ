import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

def fact(x):
    result = 1
    for i in range(x, 0, -1):
        result *= i
    return result

print(int(fact(n)//(fact(n-m)*fact(m))))
