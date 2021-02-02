def is_oneNumber(x):
    x = list(map(int, str(x)))
    if len(x) <= 2:
        return True
    elif len(x) == 3:
        if x[1]-x[0] == x[2]-x[1]:
            return True
        else:
            return False

n = int(input())
cnt = 0
for i in range(1, n+1):
    if is_oneNumber(i) == True:
        cnt += 1

print(cnt)
