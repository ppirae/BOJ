a = []
for i in range(3):
    a.append(int(input()))

if a[0] + a[1] + a[2] == 180:
    if a[0] == 60 and a[1] == 60 and a[2] == 60:
        print("Equilateral")
    elif a[0] == a[1]:
        print("Isosceles")
    elif a[1] == a[2]:
        print("Isosceles")
    elif a[0] == a[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
