s = input().upper()
cnt = [0 for i in range(26)]
result = []
index = []
for ch in s:
    for i in range(65, 91):
        if ch == chr(i):
            cnt[i-65] += 1

for i in range(26):
    if cnt[i] == max(cnt):
        result.append(cnt[i])
        index.append(i)

if len(result) != 1:
    print("?")
else:
    print(chr(int(index[0])+65))
