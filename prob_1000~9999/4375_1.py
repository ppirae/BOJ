while True:
    try:
        n = int(input())
    except EOFError:
        break
    res = 1
    while True:
        if res % n == 0:
            print(len(str(res)))
            break
        res = res * 10 + 1