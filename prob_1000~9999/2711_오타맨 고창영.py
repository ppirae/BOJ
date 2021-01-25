n = int(input())

for i in range(n):
    result = ''
    data = input().split()
    for j in range(len(data[1])):
        if j != int(data[0])-1:
            result += data[1][j]
        else:
            continue
    print(result)
