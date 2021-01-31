arr = [[] for _ in range(9)]
max = 0
index_i = 0
index_j = 0
for i in range(9):
    arr[i] = input().split()

for i in range(9):
    for j in range(9):
        if int(arr[i][j]) > max:
            max = int(arr[i][j])
            index_i = i+1
            index_j = j+1

print(max)
print(index_i, index_j)
