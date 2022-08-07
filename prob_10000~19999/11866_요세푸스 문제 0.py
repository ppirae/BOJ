n, k = map(int, input().split())

result = 0

for i in range(1, n+1):
    result = (result + k) % i
    print(result + 1)