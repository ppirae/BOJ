arr = sorted(list(map(int, input().split())))
A = arr[0]
B = arr[1]
C = arr[2]
result = []
words = input()
for word in words:
    if word == "A":
        result.append(arr[0])
    elif word == "B":
        result.append(arr[1])
    else:
        result.append(arr[2])

for i in result:
    print(i, end = ' ')
