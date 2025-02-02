# 100만보다 작고 2이상의 약수를 가지고 있다면, 틀린 비밀번호

TC = int(input())

for _ in range(TC):
    number = int(input())

    for i in range(2, 1_000_001):
        if number % i == 0: # 100만 이하의 약수가 존재한다.
            print("NO")
            break
        if i == 1_000_000: # 100만 이하의 약수가 존재하지 않는다.
            print("YES")

# 앞으로 만나게 될 모든 문제를
# 일단! 완전탐색, 모든 경우의 수를 넣어준다.