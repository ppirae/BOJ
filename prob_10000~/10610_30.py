import sys
n = list(map(int, input()))

def is_30(x):
    sum = 0
    result = ''
    for i in x:
        sum += i
    if sum % 3 == 0:
        x.sort(reverse=True)
        if x[len(x)-1] == 0:
            for j in range(len(x)):
                result += str(x[j])
            print(result)
        else:
            print("-1")
    else:
        print("-1")

is_30(n)
