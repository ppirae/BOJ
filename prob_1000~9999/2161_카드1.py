import sys
from collections import  deque
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)

while len(q) != 1:
    n = q.popleft()
    print(n, end = ' ')
    n2 = q.popleft()
    q.append(n2)

print(q.pop())
