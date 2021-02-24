t = int(input())
for i in range(t):
    data = input().split()
    if data[1] == "+":
        answer = int(data[0]) + int(data[2])
    elif data[1] == "-":
        answer = int(data[0]) - int(data[2])
    elif data[1] == "*":
        answer = int(data[0]) * int(data[2])
    else:
        answer = int(data[0]) / int(data[2])

    if answer == int(data[4]):
        print("correct")
    else:
        print("wrong answer")
