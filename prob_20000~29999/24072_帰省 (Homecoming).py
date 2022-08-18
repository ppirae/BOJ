a, b, c = map(int, input().split())
arr = [False] * 101
for i in range(a, b):
    arr[i] = True
print(1 if arr[c] == True else 0)