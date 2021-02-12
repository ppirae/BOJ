import math
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    big, small = 0, 0
    if r2 > r1:
        big = r2
        small = r1
    else:
        big = r1
        small = r2

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if d > big - small and d < big + small:
            print(2)
        elif d == (big - small):
            print(1)
        elif d == (big + small):
            print(1)
        elif d < big - small:
            print(0)
        elif d > big + small:
            print(0)
        elif d == 0 and big != small:
            print(0)
