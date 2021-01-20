s = input()
cnt = 0
result = ''
for word in s:
    cnt += 1
    result += word
    if cnt % 10 == 0:
        result += '\n'

print(result)
