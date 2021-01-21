import sys
n, m = map(str, sys.stdin.readline().split())
n = list(n)
m = list(m)
sum_n = 0
sum_m = 0
for i in n:
    sum_n += int(i)
for i in m:
    sum_m += int(i)

print(sum_n*sum_m)
