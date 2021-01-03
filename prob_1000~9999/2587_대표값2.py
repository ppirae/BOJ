l = [0 for i in range(5)]

for i in range(5):
    l[i] = int(input())

avg = 0
mid = 0

avg = sum(l)/5
l.sort()
mid = l[2]
print(int(avg))
print(mid)
