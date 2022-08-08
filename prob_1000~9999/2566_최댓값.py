board = [[] for _ in range(9)]
for i in range(9):
    board[i] = list(map(int, input().split()))

max = -21470000000

for i in range(9):
    for j in range(9):
        if board[i][j] > max:
            max = board[i][j]
            a = i
            b = j

print(max)
print(a+1, b+1)