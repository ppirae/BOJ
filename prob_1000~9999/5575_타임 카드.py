a1, b1, c1, d1, e1, f1 = map(int, input().split())
a2, b2, c2, d2, e2, f2 = map(int, input().split())
a3, b3, c3, d3, e3, f3 = map(int, input().split())

total1 = (d1*3600 + e1*60 + f1) - (a1*3600 + b1*60 + c1)
total2 = (d2*3600 + e2*60 + f2) - (a2*3600 + b2*60 + c2)
total3 = (d3*3600 + e3*60 + f3) - (a3*3600 + b3*60 + c3)

def time(sum):
    print(sum//3600, end = ' ')
    sum %= 3600
    print(sum//60, end = ' ')
    sum %= 60
    print(sum)

time(total1)
time(total2)
time(total3)