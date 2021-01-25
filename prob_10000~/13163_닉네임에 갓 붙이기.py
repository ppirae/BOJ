n = int(input())
for i in range(n):
    data = input().split()
    data[0] = "god"
    for i in range(len(data)):
        print(data[i], end = '')
    print()
