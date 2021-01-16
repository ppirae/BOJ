import sys
n = str(bin(int(sys.stdin.readline())))[2:][::-1]
print(int(n, 2))
