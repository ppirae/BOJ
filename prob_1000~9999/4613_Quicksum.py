import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "#":
        break
    sum = 0
    for i in range(len(s)):
        if s[i] == " ":
            sum += 0
        else:
            tmp = ord(s[i])-64
            sum += ((i+1) * tmp)
    print(sum)