import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    d = [0] * 11
    d[0] = 1
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]
    print(d[n])
