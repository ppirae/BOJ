import sys

tmp = ['C','A','M','B','R','I','D','G','E']
s = sys.stdin.readline()
ans = ''
for i in range(len(s)-1):
    if not s[i] in tmp:
        ans += s[i]

print(ans)
