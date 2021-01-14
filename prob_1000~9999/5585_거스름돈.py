n = 1000 - int(input())

coin_types = [500,100,50,10,5,1]
cnt = 0

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)
