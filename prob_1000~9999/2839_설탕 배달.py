n = int(input())

if n == 4 or n == 7:
    print(-1)
else:
    if n % 5 == 0:
        print(n // 5)
    elif n % 5 == 1:
        print(n // 5 + 1)
    elif n % 5 == 2:
        print(n // 5 + 2)
    elif n % 5 == 3:
        print(n // 5 + 1)
    else:
        print(n // 5 + 2)