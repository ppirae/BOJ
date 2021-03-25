import sys
from math import gcd
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(":"))
print(str(n//gcd(n, m)) + ":" + str(m//gcd(n, m)))
