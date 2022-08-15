import sys
input = sys.stdin.readline

n = int(input().strip())
tree = [[0] * n for _ in range(n)]
res = [-1 * (n+1)]
print(tree)
print(res)
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a] = [b]
    tree[b] = [a]

print(tree)