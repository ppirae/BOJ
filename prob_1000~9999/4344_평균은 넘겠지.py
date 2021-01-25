n = int(input())
for i in range(n):
    data = input().split()
    cnt = 0
    per = 0
    arr = [0 for i in range(int(data[0]))]
    for j in range(1, len(data)):
        arr.append(int(data[j]))

    for k in range(len(arr)):
        if arr[k] > sum(arr)/(len(data)-1):
            cnt += 1
    per = (cnt / (len(data)-1)) * 100
    print("%.3f" % per+"%")
