# A가 정답으로 생각할 수 있는 모든 수를 넣어보기

# 그리고 B가 도전한 내용에 맞는지 확인하기

n = int(input())
ans = 0

hint = [list(map(int, input().split())) for _ in range(n)]

# 100~999
for a in range(1, 10):  # 100의 자리수
    for b in range(1, 10):  # 10의 자리수
        for c in range(1, 10):  # 1의 자리수
            if (a == b or b == c or c == a):
                continue

            # 숫자가 정해졌다면
            cnt = 0
            for arr in hint:
                number = arr[0]
                strike = arr[1]
                ball = arr[2]

                # a,b,c 라는 숫자를
                # number 하고 비교해서
                ball_count = 0
                strike_count = 0

                # 자리수를 나눠서, strike, ball을 측정하는 부분
                if (number // 100) == a:
                    strike_count += 1
                elif (number // 100) == b:
                    ball_count += 1
                elif (number // 100) == c:
                    ball_count += 1

                if ((number % 100) // 10) == a:
                    ball_count += 1
                elif ((number % 100) // 10) == b:
                    strike_count += 1
                elif ((number % 100) // 10) == c:
                    ball_count += 1

                if (number % 10) == a:
                    ball_count += 1
                elif (number % 10) == b:
                    ball_count += 1
                elif (number % 10) == c:
                    strike_count += 1

                if ball == ball_count and strike == strike_count:
                    cnt += 1
            if cnt == n:
                ans += 1
print(ans)
