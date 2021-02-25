import sys
input = sys.stdin.readline

d = [0] * 1000001
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 1000001):
    d[i] = (d[i-3] + d[i-2] + d[i-1]) % 1000000009

t = int(input())
for i in range(t):
    n = int(input())
    print(d[n])
