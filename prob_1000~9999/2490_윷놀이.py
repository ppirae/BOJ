def f(n):
    if sum(n)==1:
        return "C"
    elif sum(n)==2:
        return "B"
    elif sum(n)==3:
        return "A"
    elif sum(n)==4:
        return "E"
    else:
        return "D"

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
print(f(a))
print(f(b))
print(f(c))
