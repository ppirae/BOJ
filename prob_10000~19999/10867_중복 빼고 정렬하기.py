n = int(input())
arr = list(map(int,input().split()))

for i in sorted(list(set(arr))):
    print(i, end = ' ')
