n = int(input())
price = []
for i in range(n):
    price.append(float(input())*0.8)

for i in range(n):
    print("${0:0.2f}".format(price[i]))
