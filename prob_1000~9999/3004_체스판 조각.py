n = int(input())

if n <= 1:
    print("2")
else:
    if n%2 == 0:
        print(((n//2)+1)*((n//2)+1))
    else:
        print(((n//2)+2)*((n//2)+1))
