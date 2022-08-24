import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "#":
        break
    res = ""
    for i in s:
        if i == " ":
            res += "%20"
        elif i == "!":
            res += "%21"
        elif i == "$":
            res += "%24"
        elif i == "%":
            res += "%25"
        elif i == "(":
            res += "%28"
        elif i == ")":
            res += "%29"
        elif i == "*":
            res += "%2a"
        else:
            res += i
    print(res)