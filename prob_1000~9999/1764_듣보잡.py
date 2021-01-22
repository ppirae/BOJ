import sys
n, m = map(int,sys.stdin.readline().split())
a = []
b = []
for i in range(n):
    a.append(sys.stdin.readline())
for i in range(m):
    b.append(sys.stdin.readline())

a = set(a)
b = set(b)
result = sorted(list(a&b))

print(len(result))
for i in range(len(result)):
    print(result[i])
