x, y = map(int, input().split())
a = x + y
b = x - y
if a > b:
    print(a)
    print(b)
else:
    print(b)
    print(a)