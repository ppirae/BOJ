import sys
t = int(input())
win_a = 0
win_b = 0
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        win_a += 1
    elif a < b:
        win_b += 1
    else:
        continue

print(win_a, win_b)
