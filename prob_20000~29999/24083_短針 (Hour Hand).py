a = int(input())
b = int(input())

b = b%12
a += b
if a > 12:
    a -= 12

print(a)