import sys
S = set()
t = int(sys.stdin.readline())
for i in range(t):
    data = sys.stdin.readline().split()
    if len(data) == 2:
        data[1] = int(data[1])
    if data[0] == "add":
        if data[1] not in S:
            S.add(data[1])
    elif data[0] == "remove":
        try:
            S.remove(data[1])
        except:
            pass
    elif data[0] == "check":
        if data[1] in S:
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        if data[1] in S:
            S.remove(data[1])
        else:
            S.add(data[1])
    elif data[0] == "all":
        S = set(range(1, 21))
    else:
        S.clear()
