import sys
sys.setrecursionlimit(9999999)

n, m = map(int,input().split())
res = [0] * m

def DFS(L):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if L == 0 or res[L-1] <= i:
                res[L] = i
                DFS(L+1)

DFS(0)