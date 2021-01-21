while True:
    s = input()
    if s == "EOI":
        break
    else:
        if s.lower().count("nemo") != 0:
            print("Found")
        else:
            print("Missing")
