while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    res = ""
    for i in range(1, n):
        if n%i == 0:
           arr.append(i)
    if sum(arr) == n:
        res = str(n) + " = "
        for j in arr:
            res += str(j) + " + "
        print(res[:-3])
    else:
        print(str(n) + " is NOT perfect.")