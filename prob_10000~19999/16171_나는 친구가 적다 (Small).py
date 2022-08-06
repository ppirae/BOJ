s = input()
answer = input()
new = []

for i in s:
    if i.isalpha():
        new.append(i)

new = ''.join(new)

if answer in new:
    print(1)
else:
    print(0)