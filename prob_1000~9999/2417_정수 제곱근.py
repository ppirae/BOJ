import sys
input = sys.stdin.readline

n = int(input())
sqrt = n ** 0.5

if sqrt % 1 == 0:
    print(int(sqrt))
else:
    print(int(sqrt)+1)
