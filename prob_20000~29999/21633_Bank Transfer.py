n = int(input())
res = 25 + 0.01*n
if res < 100:
    res = 100
elif res > 2000:
    res = 2000

print("%.2f" % res)