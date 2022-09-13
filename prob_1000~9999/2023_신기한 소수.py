# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

import math

n = int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            else:
                if isPrime(number * 10 + i):
                    DFS(number * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)