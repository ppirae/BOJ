arr = []
for i in range(4):
    arr.append(int(input()))

if len(set(arr)) == 1:
    print("Fish At Constant Depth")
elif arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3]:
    print("Fish Diving")
elif arr[0] < arr[1] and arr[1] < arr[2] and arr[2]< arr[3]:
    print("Fish Rising")
else:
    print("No Fish")