result = []
for i in range(5):
    arr = list(map(int, input().split()))
    result.append(sum(arr))

print(result.index(max(result))+1, max(result))
