a, b, c = map(int, input().split())
x = (b-a)%c
if x == 0:
    print((b-a)//c)
else:
    print((b-a)//c + 1)