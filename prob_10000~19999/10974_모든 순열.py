from itertools import permutations
n = int(input())
arr = list(permutations(range(1, n+1),n))
for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
