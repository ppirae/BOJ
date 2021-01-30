import sys
t = int(input())
for i in range(t):
    alpha = [0] * 26
    sum = 0
    words = sys.stdin.readline()
    for word in words:
        for j in range(26):
            if word == chr(65+j):
                alpha[j] = 1
            else:
                continue
    for k in range(len(alpha)):
        if alpha[k] == 0:
            sum += 65 + k

    print(sum)
