def fact(x):
    result = 1
    for i in range(x, 0, -1):
        result *= i
    return result

n, k = map(int,input().split())
print(int(fact(n)/(fact(n-k)*fact(k))))
