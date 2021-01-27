t = int(input())
for i in range(t):
    space = input()
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(int(input()))
    if sum(arr) % n == 0:
        print("YES")
    else:
        print("NO")
