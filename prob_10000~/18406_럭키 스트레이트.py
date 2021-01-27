data = list(map(int, input()))
left_side = []
right_side = []

mid = len(data)//2
for i in range(0, mid):
    left_side.append(data[i])
for j in range(mid, len(data)):
    right_side.append(data[j])

if sum(left_side) == sum(right_side):
    print("LUCKY")
else:
    print("READY")
