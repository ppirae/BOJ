while True:
    arr = list(input().split())
    if arr[0] == "#" and int(arr[1]) == 0 and int(arr[2]) == 0:
        break
    if int(arr[1]) > 17 or int(arr[2]) >= 80:
        print(arr[0] + " Senior")
    else:
        print(arr[0] + " Junior")