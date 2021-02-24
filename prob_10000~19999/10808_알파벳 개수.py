s = input()
result = [0 for i in range(26)]
for word in s:
    for j in range(97,123):
        if word == chr(j):
            result[j-97] += 1

for i in range(len(result)):
    print(result[i], end = ' ')
