n = int(input())
for i in range(n):
    words = list(map(str, input()))
    result = ''
    for j in range(len(words)):
        if j == 0:
            if words[j].islower():
                words[j] = words[j].upper()
            else:
                break
        else:
            break
    for k in range(len(words)):
        result += words[k]
    print(result)
