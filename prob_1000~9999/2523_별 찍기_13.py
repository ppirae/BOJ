n = int(input())

for i in range(n):
    for j in range(0,i+1):
        print("*",end='')
    print("\n",end='')

for i in range(n):
    for k in range(n-1,i,-1):
        print("*",end='')
    print("\n",end='')
