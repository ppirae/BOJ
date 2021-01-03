s = input()
result = ''
for word in s:
    if word.islower():
        word = word.upper()
        result += word
    else:
        word = word.lower()
        result += word

print(result)
