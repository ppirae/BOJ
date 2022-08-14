a, b = map(int, input().split())

MAX = max(a, b)
MIN = min(a, b)

n = MAX - MIN

s = (n * (n+1) // 2)
print(s + (MIN) * (n+1))