self_number = [True] * 11000
i = 1
while True:
    hap = sum(list(map(int, str(i))))
    constructor = i + hap
    if constructor > 11000:
        break
    else:
        self_number[constructor] = False
    i += 1

for i in range(len(self_number)):
    if i != 0:
        if self_number[i] == True and i < 10000:
            print(i)
