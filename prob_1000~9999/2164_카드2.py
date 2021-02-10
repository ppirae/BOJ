from collections import  deque

n = int(input())
list = deque()
for i in range(1, n+1):
    list.append(i)

while len(list) != 1:
    list.popleft()
    a = list.popleft()
    list.append(a)

print(list[0])
