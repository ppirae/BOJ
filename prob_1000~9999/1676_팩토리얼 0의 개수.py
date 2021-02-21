n = int(input())

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return list(map(int, str(result)))

arr = fact(n)[::-1]
cnt = 0
for i in arr:
    if i == 0:
        cnt += 1
    else:
        break

print(cnt)
