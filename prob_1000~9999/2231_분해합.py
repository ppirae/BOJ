n = int(input())

def f(x):
    for i in range(1, x):
        sum = i
        arr = list(map(int, str(i)))
        for j in range(len(arr)):
            sum += arr[j]
        if sum == x:
            return i
            break

if f(n) == None:
    print(0)
else:
    print(f(n))
