a, b, c = map(int, input().split())
find = 0
while find == 0:
    if (a+b) == c:
        print(str(a)+"+"+str(b)+"="+str(c))
        find = 1
    elif (a-b) == c:
        print(str(a)+"-"+str(b)+"="+str(c))
        find = 1
    elif (a*b) == c:
        print(str(a)+"*"+str(b)+"="+str(c))
        find = 1
    elif (a//b) == c:
        print(str(a)+"/"+str(b)+"="+str(c))
        find = 1
    elif (b+c) == a:
        print(str(a)+"="+str(b)+"+"+str(c))
        find = 1
    elif (b-c) == a:
        print(str(a)+"="+str(b)+"-"+str(c))
        find = 1
    elif (b*c) == a:
        print(str(a)+"="+str(b)+"*"+str(c))
        find = 1
    elif (b//c) == a:
        print(str(a)+"="+str(b)+"/"+str(c))
        find = 1