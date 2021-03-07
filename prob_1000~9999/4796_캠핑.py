import sys
input = sys.stdin.readline

cnt = 0
while True:
    L, P, V = map(int, input().rstrip().split())
    cnt += 1
    if L == 0 and P == 0 and V == 0:
        break
    else:
        if V%P > L:
            result = (V//P)*L + L
        else:
            result = (V//P)*L + V%P
        print("Case",str(cnt)+":", result)
