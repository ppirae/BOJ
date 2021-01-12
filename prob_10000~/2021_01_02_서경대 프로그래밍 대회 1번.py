def solution(src):
    answer = ''
    cnt = 0
    src = list(map(int,src))
    print(src)
    if src[0] == 0:
        answer += "0"
    else:
        answer += "1"
    for i in range(len(src)-1):
        if src[i] == src[i+1]:
            cnt += 1
            if i == len(src)-2:
                 answer += chr(cnt+65)
        else:
            answer += chr(cnt+65)
            cnt = 0
            continue
    print(cnt)

    return answer
