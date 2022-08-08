n, m = map(int, input().split())

dogam = dict()
for i in range(1, n+1):
    dogam[i] = input()

dogam2 = {v:k for k, v in dogam.items()}

for i in range(m):
    s = input()
    if s.isnumeric():
        print(dogam.get(int(s)))
    else:
        print(dogam2.get(s))