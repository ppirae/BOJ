s = input()
result = []
for i in range(len(s)):
    result.append(s[i:])

result = sorted(result)
for i in range(len(result)):
    print(result[i])
