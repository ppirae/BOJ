import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [[] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().rstrip().split()))

n2, m2 = map(int, input().rstrip().split())
b = [[] for i in range(n2)]
for i in range(n2):
    b[i] = list(map(int, input().rstrip().split()))

c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            c[i][j] += (a[i][k] * b[k][j])

for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j], end = ' ')
    print()
