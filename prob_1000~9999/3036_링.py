import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

for i in range(1, n):
    gcd = 0
    a = 0
    b = 0
    for j in range(1, arr[i]+1):
        if arr[0]%j == 0 and arr[i]%j == 0:
            gcd = j
    print(str(arr[0]//gcd) + "/" + str(arr[i]//gcd))
