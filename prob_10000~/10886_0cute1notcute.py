n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

if a.count(1) > a.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
