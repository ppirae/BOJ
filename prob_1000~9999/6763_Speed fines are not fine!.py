a = int(input())
b = int(input())
over = b-a
if b <= a:
    print("Congratulations, you are within the speed limit!")
else:
    if 1 <= over <= 20:
        print("You are speeding and your fine is $100.")
    elif 21 <= over <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")