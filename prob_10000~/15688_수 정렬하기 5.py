import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(len(arr)):
    print(arr[i])
