n = int(input())
for i in range(n):
    result = ''
    data = input().split()
    for ch in data[1]:
        result += ch*int(data[0])
    print(result)
