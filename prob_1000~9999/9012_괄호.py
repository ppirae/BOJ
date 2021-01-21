import sys
n = int(sys.stdin.readline())

def is_VPS(s):
    stack = []
    for ps in s[:-1]:
        if ps == "(":
            stack.append(ps)
        elif ps == ")" and stack == []:
            return False
        else:
            stack.pop()

    if stack == []:
        return True
    else:
        return False

for i in range(n):
    s = sys.stdin.readline()
    if is_VPS(s):
        print("YES")
    else:
        print("NO")
