h, m = map(int,input().split())

if h == 0:
    if m >= 45:
        m -= 45
    else:
        h = 23
        m += 15
else:
    if m >= 45:
        m -= 45
    else:
        h -= 1
        m += 15

print(h,m)
