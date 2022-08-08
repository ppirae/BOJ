import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))

ab = set1.difference(set2)
ba = set2.difference(set1)
c = ab.union(ba)

print(len(c))