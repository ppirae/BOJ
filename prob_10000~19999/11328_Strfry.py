n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    a = sorted(list(a))
    b = sorted(list(b))
    if a == b:
        print("Possible")
    else:
        print("Impossible")
