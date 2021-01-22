n = int(input())
for i in range(n):
    a = ['' for i in range(2)]
    s = input().split()
    a[0] = sorted(list(s[0]))
    a[1] = sorted(list(s[1]))
    if a[0] == a[1]:
        print(s[0], "&", s[1], "are anagrams.")
    else:
        print(s[0], "&", s[1], "are NOT anagrams.")
