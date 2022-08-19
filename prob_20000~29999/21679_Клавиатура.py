n = int(input())
arr = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    arr[i-1] -= 1

for i in arr:
    if i < 0:
        print('yes')
    else:
        print('no')