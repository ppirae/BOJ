# 스택
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

num = 1
stk = []
ans = ''
flag = True

for i in range(n):
    now = arr[i]
    if now >= num:
        while now >= num:
            stk.append(num)
            num += 1
            ans += "+\n"
        stk.pop()
        ans += "-\n"
    elif now < num:
        top = stk.pop()
        if top > now:
            flag = False
            print("NO")
            break
        else:
            ans += "-\n"

if flag:
    print(ans)