import math
N,W,H,L = map(int,input().split())
sum = 0
sum = (math.floor(W/L)*math.floor(H/L))
if sum < N:
    print(sum)
else:
    print(N)
