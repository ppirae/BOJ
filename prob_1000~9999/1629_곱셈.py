def pow(x, n):
    if n == 0:
        return 1
    else:
        tmp = pow(x, n//2)
        if n % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * a % c

a, b, c = map(int, input().split())
result = pow(a, b)
print(result)
