import sys
input = sys.stdin.readline

t = int(input())

zero = []
one = []
plus = []
minus = []

for i in range(t):
    n = int(input())
    if n == 0:
        zero.append(n)
    elif n == 1:
        one.append(n)
    elif n < 0 :
        minus.append(n)
    else:
        plus.append(n)

plus.sort(reverse=True)
minus.sort()

answer = 0

def tie_sum(li):
    SUM = 0
    for i in range(0, len(li)-1, 2):
        temp = (li[i] * li[i+1])
        SUM += temp
    return SUM

if len(plus) % 2 == 0:
    answer += tie_sum(plus)
else:
    answer += (tie_sum(plus) + plus[-1])

if len(zero) == 0:
    if len(minus) % 2 == 0:
        answer += tie_sum(minus)
    else:
        answer += (tie_sum(minus) + minus[-1])
else:
    if len(minus) % 2 == 0:
        answer += tie_sum(minus)
    else:
        answer += (tie_sum(minus) + (minus[-1] * 0))

answer += len(one)

print(answer)