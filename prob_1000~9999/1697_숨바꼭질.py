from collections import deque

n, m = map(int, input().split())

Q = deque()
Q.append(n)
MAX = 100000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
ch[n] = 1
while Q:
    now = Q.popleft()
    if now == m:
        break
    for i in (now-1, now+1, 2*now):
        if 0 <= i <= MAX:
            if ch[i] == 0:
                ch[i] = 1
                Q.append(i)
                dis[i] = dis[now] + 1

print(dis[m])