import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = 1
SUM = 1
cnt = 1

while end != n:
    if SUM == n:
        cnt += 1
        end += 1
        SUM += end
    elif SUM > n:
        SUM -= start
        start += 1
    elif SUM < n:
        end += 1
        SUM += end

print(cnt)