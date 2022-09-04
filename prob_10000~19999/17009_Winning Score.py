arr1 = []
arr2 = []
for _ in range(3):
    arr1.append(int(input()))
for _ in range(3):
    arr2.append(int(input()))

sum1 = arr1[0]*3 + arr1[1]*2 + arr1[2]
sum2 = arr2[0]*3 + arr2[1]*2 + arr2[2]

if sum1 > sum2:
    print('A')
elif sum1 < sum2:
    print('B')
else:
    print('T')