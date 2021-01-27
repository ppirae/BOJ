n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n):
    print(str(i+1) + ". " + arr[i])
