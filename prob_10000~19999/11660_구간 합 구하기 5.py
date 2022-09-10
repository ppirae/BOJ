import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)]
S = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]

for i in range(m):
    s1, e1, s2, e2 = map(int, input().split())
    print(S[s2][e2] - S[s2][e1-1] - S[s1-1][e2] + S[s1-1][e1-1])