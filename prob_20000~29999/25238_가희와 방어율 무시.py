a, b = map(int, input().split())
d = a - (a * (b/100))
if d >= 100:
    print(0)
else:
    print(1)