t = int(input())
result = []

def is_groupWord(s):
    sum = ''
    for i in range(len(s)):
        if i == 0:
            sum += s[i]
        else:
            if sum[-1] != s[i] and s[i] in sum:
                return False
            else:
                sum += s[i]
    return True

for i in range(t):
    words = input()
    result.append(is_groupWord(words))

print(result.count(True))
