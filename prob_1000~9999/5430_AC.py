import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for i in range(t):
    order = input().rstrip()
    n = int(input())
    if n == 0:
        arr = deque(input().rstrip())
        arr = deque()
    else:
        arr = deque(input().rstrip()[1:-1].split(','))

    r_cnt = 0
    flag = 0
    for o in order:
        if o == "R":
            r_cnt += 1
        else:
            if not arr:
                flag = 1
            else:
                if r_cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if r_cnt % 2 != 0:
        arr.reverse()

    if flag == 1:
        print("error")
    else:
        print("[" + ','.join(list(arr)) + "]")