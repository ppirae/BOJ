import sys
from collections import  deque
deq = deque()
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        deq.append(int(s[1]))
    elif s[0] == "pop":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
            deq.popleft()
    elif s[0] == "size":
        print(len(deq))
    elif s[0] == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif s[0] == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    else:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
