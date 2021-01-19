while True:
    s = input()
    if s == "0":
        break
    else:
        reverse = s[::-1]
        if reverse == s:
            print("yes")
        else:
            print("no")
