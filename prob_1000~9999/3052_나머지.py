l = []
result = []
for i in range(10):
    l.append(int(input()))
    l[i] = l[i]%42

l.sort()
result = set(l)
print(len(result))
