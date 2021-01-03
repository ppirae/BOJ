import sys
a = int(input())
b = [0 for i in range(a)]
for i in range(a):
    b[i] = sys.stdin.readline().strip()

b.sort(key=int)
for i in range(a):
    print(b[i])
