from collections import deque

n = int(input())
s = input()
arr = deque()
for i in range(n):
    arr.append(int(input()))

stack = []

for i in s:
    if i.isalpha():
        stack.append(arr[ord(i) - ord('A')])
    else:
        if i == "*":
            a = stack.pop()
            b = stack.pop()
            c = a * b
        elif i == "+":
            a = stack.pop()
            b = stack.pop()
            c = a + b
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            c = b - a
        else:
            a = stack.pop()
            b = stack.pop()
            c = b / a
        stack.append(c)

print("%.2f" % stack[0])