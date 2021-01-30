t = int(input())
for i in range(t):
    arr = sorted(list(map(int,input().split())))
    if arr[2]**2 == arr[0]**2 + arr[1]**2:
        print("Scenario #"+str(i+1)+":\nyes")
        print()
    else:
        print("Scenario #"+str(i+1)+":\nno")
        print()
