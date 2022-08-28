t = int(input())
for i in range(t):
    n = int(input())
    t2 = int(input())
    for j in range(t2):
        a, b = map(int, input().split())
        n += (a*b)
    print(n)