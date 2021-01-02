n = int(input())

for i in range(n):
    for j in range(0,i):
        print(" ",end='')
    for k in range(n,i,-1):
        print("*",end='')
    for z in range(n-1,i,-1):
        print("*",end='')
    print()
