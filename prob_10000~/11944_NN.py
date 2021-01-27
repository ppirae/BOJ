N, M = map(str, input().split())
result = ''

while len(result) < len(N) * int(N):
    result += N
print(result[:int(M)])
