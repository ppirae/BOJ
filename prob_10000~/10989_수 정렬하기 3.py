import sys

n = int(sys.stdin.readline())
count = [0 for i in range(10000)]
for i in range(n):
    num = int(sys.stdin.readline())
    count[num-1] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i+1)
