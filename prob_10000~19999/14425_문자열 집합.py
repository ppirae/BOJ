import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for i in range(n):
    d[input()] = i

cnt = 0
for i in range(m):
    s = input()
    if s in d.keys():
        cnt += 1

print(cnt)