import sys
queue = []
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        queue.insert(0, int(s[1]))
    elif s[0] == "pop":
        if queue == []:
            print("-1")
        else:
            print(queue[-1])
            queue.pop()
    elif s[0] == "size":
        print(len(queue))
    elif s[0] == "empty":
        if queue == []:
            print("1")
        else:
            print("0")
    elif s[0] == "front":
        if queue == []:
            print("-1")
        else:
            print(queue[-1])
    else:
        if queue == []:
            print("-1")
        else:
            print(queue[0])
