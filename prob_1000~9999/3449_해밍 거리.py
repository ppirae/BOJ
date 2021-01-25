import math
n = int(input())
for i in range(n):
    cnt = 0
    a = input()
    b = input()
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print("Hamming distance is " + str(cnt) + ".")
