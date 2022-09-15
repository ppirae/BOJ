# 스택
import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

def check(stk, ch):
    stk.append(ch)
    if len(stk) < len(bomb):
        return stk
    else:
        temp = ''
        for i in range(1, len(bomb)+1):
            temp += stk[-i]
    temp = temp[::-1]
    if temp == bomb:
        for i in range(len(bomb)):
            stk.pop()
    return stk

stk = []
for i in s:
    stk = check(stk, i)

if stk == []:
    print("FRULA")
else:
    ans = ''.join(stk)
    print(ans)