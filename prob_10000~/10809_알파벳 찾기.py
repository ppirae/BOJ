s = input()
result = [-1 for i in range(26)]

for word in s:
    for i in range(97, 123):
        if word == chr(i):
            result[i-97] = s.index(word)

for i in range(len(result)):
    print(result[i], end = ' ')
