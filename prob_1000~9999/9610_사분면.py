import sys
t = int(sys.stdin.readline())
xy = [0] * 5
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        xy[0] += 1
    elif a == 0 and b > 0:
        xy[0] += 1
    elif a == 0 and b < 0:
        xy[0] += 1
    elif a > 0 and b == 0:
        xy[0] += 1
    elif a < 0 and b == 0:
        xy[0] += 1
    elif a > 0 and b > 0:
        xy[1] += 1
    elif a > 0 and b < 0:
        xy[4] += 1
    elif a < 0 and b > 0:
        xy[2] += 1
    else:
        xy[3] += 1

print("Q1:", xy[1])
print("Q2:", xy[2])
print("Q3:", xy[3])
print("Q4:", xy[4])
print("AXIS:", xy[0])
