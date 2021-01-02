n = int(input())

for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end='')
    for k in range(i+1,2*(i+1)):
        print("*",end='')
    for z in range(0,i):
        print("*",end='')
    print()
