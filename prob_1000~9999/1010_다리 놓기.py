import sys
from math import factorial
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))
