for _ in range(int(input())):
    s = input()
    cnt = 0
    for i in s:
        if i == 'U':
            cnt += 1
        else:
            break
    print(cnt)