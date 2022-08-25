import sys
sys.setrecursionlimit(99999)

x = int(input())

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

print(str(fac(x))[-1:])