import sys
n = int(sys.stdin.readline())
for i in range(31):
    if 2**i == n:
        print("1")
        break
    else:
        continue
else:
    print("0")
