t = int(input())
list = []
for i in range(t):
    x, y = map(str,input().split())
    list.append((x,y))

list = sorted(list, key = lambda x: int(x[0]))
for i in list:
    for j in i:
        print(j, end = ' ')
    print()
