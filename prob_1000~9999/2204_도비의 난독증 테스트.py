import sys
input = sys.stdin.readline

while True:
    n = int(input())
    li = []
    if n == 0:
        break
    for i in range(n):
        s = input()
        li.append(s)
    li.sort(key=lambda s:s.lower())
    print(li[0], end = '')