d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
d[6] = 3
d[7] = 4
t = int(input())
for i in range(t):
    n = int(input())
    if n <= 7:
        print(d[n])
    else:
        for i in range(8, n+1):
            d[i] = d[i-1] + d[i-5]
        print(d[n])
