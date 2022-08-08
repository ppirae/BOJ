from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n+1):
    q.append(i)

answer = "<"

while q:
    for i in range(k-1):
        rotate = q.popleft()
        q.append(rotate)
    popleft = q.popleft()
    answer += str(popleft) + ", "

answer = answer[:-2]
answer += ">"
print(answer)