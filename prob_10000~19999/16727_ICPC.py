a, b = map(int, input().split())
c, d = map(int, input().split())
p = a + d
e = b + c
if p > e:
    print("Persepolis")
elif p < e:
    print("Esteghlal")
elif p == e:
    if a < c:
        print("Persepolis")
    elif a > c:
        print("Esteghlal")
    else:
        print("Penalty")