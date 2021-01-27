import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(float(sys.stdin.readline()))

arr.sort()
for i in range(7):
    print("%.3f" % arr[i])
