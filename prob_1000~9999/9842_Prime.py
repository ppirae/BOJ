import sys
input = sys.stdin.readline

prime = [True for i in range(1000001)]
prime[1] = False
for i in range(2, 10001):
    for j in range(i * 2, 1000001, i):
        prime[j] = False

n = int(input())
result = []

for i in range(len(prime)):
    if i == 0:
        continue
    if prime[i]:
        result.append(i)

print(result[n-1])
