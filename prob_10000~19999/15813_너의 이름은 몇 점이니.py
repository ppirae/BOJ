n = int(input())
s = list(map(str, input()))
result = 0
for i in s:
    result += ord(i)-64

print(result)
