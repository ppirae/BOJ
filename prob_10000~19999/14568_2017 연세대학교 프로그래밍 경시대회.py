candy = int(input()) #6
ans = 0

for A in range(0, candy+1): # 0~6개
    for B in range(0, candy+1): # 0~6개
        for C in range(0, candy+1): # 0~6개
            if A+B+C == candy:
                if A >= B+2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            ans += 1
print(ans)