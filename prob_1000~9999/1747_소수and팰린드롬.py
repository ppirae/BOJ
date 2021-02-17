import math
n = int(input())

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def is_palindrom_number(x):
    reverse = int(str(x)[::-1])
    if reverse == x:
        return True
    else:
        return False

for i in range(n, 1010000):
    if is_prime_number(i) and is_palindrom_number(i):
        print(i)
        break
