t = int(input())
for i in range(t):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
        door = N // H
    else:
        door = (N // H) + 1
    if door < 10:
        print(int(str(floor) + "0" + str(door)))
    else:
        print(int(str(floor) + str(door)))
