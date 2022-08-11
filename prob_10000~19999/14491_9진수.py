def convert(n, base):
    res = ""
    while n > 0:
        n, mod = divmod(n, base)
        res += str(mod)
    return res[::-1]

n = int(input())
print(convert(n, 9))