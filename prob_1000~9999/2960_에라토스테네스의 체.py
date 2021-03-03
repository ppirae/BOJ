import sys
input = sys.stdin.readline

n, k = map(int, input().split())
prime = [True] * (n+1)
result = []
prime[0] = False
prime[1] = False
for i in range(2, n+1):
    if prime[i] == True:
        j = 1
        while i*j <= n:
            if prime[i*j] == False:
                j += 1
                continue
            else:
                prime[i*j] = False
                result.append(i*j)
                j += 1

print(result[k-1])
