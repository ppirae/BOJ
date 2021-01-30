import sys
t = int(sys.stdin.readline())
worklist = dict()
for i in range(t):
    s = sys.stdin.readline().split()
    if s[1] == "enter":
        worklist[s[0]] = 1
    else:
        worklist[s[0]] = 0

working = sorted(worklist.items(), key = lambda s : s[0], reverse=True)
for name, work in working:
    if work:
        print(name)
