t = int(input())
words = []
result = []
for i in range(t):
    words.append(input())

result = sorted(sorted(set(words)), key = len)
for i in result:
    print(i)
