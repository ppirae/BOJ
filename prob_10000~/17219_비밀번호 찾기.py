import sys
n, m = map(int, sys.stdin.readline().split(' '))
site = [0] * n
password = [0] * n
dict = {}
for i in range(n):
    data = sys.stdin.readline().split(' ')
    dict[data[0].rstrip()] = data[1].rstrip()

for i in range(m):
    data = sys.stdin.readline().rstrip()
    print(dict[data])
