n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    sum = 0
    for ch in s:
        if ch == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
