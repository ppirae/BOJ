t = int(input())
result = []
for i in range(t):
    a, b = map(int, input().split())
    result.append(b%a)

print(sum(result))
