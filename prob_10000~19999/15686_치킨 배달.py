n, m = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(n)]
hs = []
pz = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            hs.append((i, j))
        elif map[i][j] == 2:
            pz.append((i, j))

def distance(hs, pz):
    sum = 0
    for i in hs:
        min = 2147000000
        for j in pz:
            tmp = abs(i[0]-j[0]) + abs(i[1]-j[1])
            if tmp < min:
                min = tmp
        sum += min
    return sum

import itertools as it
min = 2147000000
for i in (it.combinations(pz, m)):
    tmp = distance(hs, i)
    if tmp < min:
        min = tmp

print(min)