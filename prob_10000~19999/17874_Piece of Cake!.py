a, b, c = map(int, input().split())
g = max(a-b, b)
s = max(a-c, c)
print(g*s*4)