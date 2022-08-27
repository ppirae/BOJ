score = [0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        score[0] += (a + b)
    elif a < b:
        score[1] += (a + b)
    else:
        score[0] += a
        score[1] += b
print(score[0], score[1])