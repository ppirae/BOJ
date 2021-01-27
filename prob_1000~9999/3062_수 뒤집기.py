t = int(input())
for i in range(t):
    n = int(input())
    n = n + int(str(n)[::-1])
    reverse = int(str(n)[::-1])
    if n == reverse:
        print("YES")
    else:
        print("NO")
