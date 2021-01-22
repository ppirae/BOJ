m, d = map(int,input().split())
yoil = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
for i in range(m):
    total += month[i]

total += d
a = total % 7
print(yoil[a])
