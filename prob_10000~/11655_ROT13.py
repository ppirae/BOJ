s = input()
result = ''
for ch in s:
    if ch.isdigit() or ch == " ":
        result += ch
    else:
        if ch.isupper():
            if ord(ch)+13 > 90:
                result += chr(64+ord(ch)+13-90)
            else:
                result += chr(ord(ch)+13)
        else:
            if ord(ch)+13 > 122:
                result += chr(96+ord(ch)+13-122)
            else:
                result += chr(ord(ch)+13)

print(result)
