import sys
from math import factorial
input = sys.stdin.readline

a, b = map(int, input().split())
print(factorial(a-1)//(factorial(b-1)*factorial((a-1)-(b-1))))
