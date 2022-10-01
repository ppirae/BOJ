import sys
input = sys.stdin.readline

n = int(input())
body = []
ans = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

for i in range(n):
    cnt = 0
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt += 1
    ans.append(cnt + 1)

for i in ans:
    print(i, end = ' ')