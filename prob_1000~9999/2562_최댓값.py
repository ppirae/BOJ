list = [0 for i in range(9)]

for i in range(0,9):
    list[i] = input()
    list[i] = int(list[i])

max = list[0]
for i in range(len(list)):
    if max<list[i]:
        max = list[i]
    else:
        continue;
print(max,(list.index(max)+1))
