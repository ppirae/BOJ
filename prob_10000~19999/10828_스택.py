import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        stack.append(int(s[1]))
    elif s[0] == "pop":
        if stack == []:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif s[0] == "size":
        print(len(stack))
    elif s[0] == "empty":
        if stack == []:
            print("1")
        else:
            print("0")
    else:
        if stack == []:
            print("-1")
        else:
            print(stack[-1])
