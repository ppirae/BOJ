name = ['' for i in range(5)]
for i in range(5):
    name[i] = input().count("FBI")

for i in range(5):
    if name[i] != 0:
        print(i+1, end = ' ')

if name == [0,0,0,0,0]:
    print("HE GOT AWAY!")
