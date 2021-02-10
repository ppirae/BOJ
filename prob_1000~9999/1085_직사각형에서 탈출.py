x, y, w, h = map(int,input().split())
min_x = 0
min_y = 0

if w-x < x:
    min_x = w-x
else:
    min_x = x

if h-y < y:
    min_y = h-y
else:
    min_y = y

if min_x > min_y:
    print(min_y)
else:
    print(min_x)
