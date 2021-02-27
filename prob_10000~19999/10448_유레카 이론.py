import sys
input = sys.stdin.readline

cnt = 2
num = 1
tri_num = []
while num <= 1000:
    tri_num.append(num)
    num += cnt
    cnt += 1

t = int(input())
for i in range(t):
    n =  int(input())
    result = 0
    for x in range(len(tri_num)):
        for y in range(len(tri_num)):
            for z in range(len(tri_num)):
                if tri_num[x] + tri_num[y] + tri_num[z] == n:
                    result = 1
                    break
    print(result)
