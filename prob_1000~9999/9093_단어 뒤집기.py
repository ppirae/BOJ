n = int(input())

for i in range(n):
    data = input().split()
    for i in range(len(data)):
        data[i] = str(data[i])[::-1]

    for i in range(len(data)):
        print(data[i], end = ' ')
    print()
