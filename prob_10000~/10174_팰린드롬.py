n = int(input())
for i in range(n):
    s = input().lower()
    reverse = s[::-1]
    if s == reverse:
        print("Yes")
    else:
        print("No")
