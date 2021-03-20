import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    n = reversed(str(bin(n)[2:]))
    s = list(map(int, n))
    for j in range(len(s)):
        if s[j] == 1:
            print(j, end = ' ')
