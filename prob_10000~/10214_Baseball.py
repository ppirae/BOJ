n = int(input())
for i in range(n):
    Y = []
    K = []
    for j in range(9):
        a, b = map(int, input().split())
        Y.append(a)
        K.append(b)
    if sum(Y) > sum(K):
        print("Yonsei")
    elif sum(Y) < sum(K):
        print("Korea")
    else:
        print("Draw")
