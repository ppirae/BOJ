def LCM(x, y):
    gcd = 1
    lcm = 0
    for i in range(1, y+1):
        if x%i == 0 and y%i == 0:
            gcd = i
        else:
            continue
    lcm = (x//gcd) * (y//gcd) * gcd
    return lcm

t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    print(LCM(a, b))
