import sys
for i in range(3):
    n = int(input())
    result = []
    for j in range(n):
        result.append(int(sys.stdin.readline()))
    if sum(result) > 0:
        print("+")
    elif sum(result) < 0:
        print("-")
    else:
        print("0")
