while True:
    cnt = 0
    s = input()
    if s == "#":
        break
    else:
        s = s.lower()
        for word in s:
            if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
                cnt += 1
    print(cnt)
