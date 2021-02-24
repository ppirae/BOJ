n = int(input())
d = [0] * 82
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 3
d[5] = 5
d[6] = 8
for i in range(7, n+2):
    d[i] = d[i-1] + d[i-2]

print(2 * (d[n] + d[n+1]))
