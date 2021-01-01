n, k = map(int,input().split(" "))
coins = [0 for i in range(n)]
result = 0

for i in range(n):
    coins[i] = int(input())

coins.sort(reverse=True)

for coin in coins:
    result += k//coin
    k %= coin

print(result)
