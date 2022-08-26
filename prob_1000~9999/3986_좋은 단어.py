res = 0
for _ in range(int(input())):
    s = input()
    stk = []
    for i in s:
        if not stk:
            stk.append(i)
        else:
            if stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
    if len(stk) == 0:
        res += 1
print(res)