W = []
K = []
W_sum, K_sum = 0, 0

for i in range(10):
    W.append(int(input()))
for j in range(10):
    K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)
W_sum = W[0] + W[1] + W[2]
K_sum = K[0] + K[1] + K[2]
print(W_sum, K_sum)
