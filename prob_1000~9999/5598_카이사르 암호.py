s = input()
result = ''
for ch in s:
    if ord(ch) < 68:
        ch = chr(ord(ch)+23)
        result += ch
    else:
        ch = chr(ord(ch)-3)
        result += ch

print(result)
