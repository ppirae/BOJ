t = int(input())
for i in range(t):
    n = int(input())
    player = dict()
    for j in range(n):
        data = input().split()
        player[data[1]] = int(data[0])
    salrary = sorted(player.items(), key = lambda s:s[1], reverse=True)
    print(salrary[0][0])
