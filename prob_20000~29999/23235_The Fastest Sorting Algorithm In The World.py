cnt = 0
while True:
    s = input()
    if s == "0" or s == 0:
        break
    cnt += 1

for i in range(1, cnt+1):
    print("Case " + str(i) + ": Sorting... done!")