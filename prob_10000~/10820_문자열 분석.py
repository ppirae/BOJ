import sys
while True:
    words = sys.stdin.readline()

    if not words:
        break

    cnt = [0] * 4
    for word in words:
        if word.islower():
            cnt[0] += 1
        elif word.isupper():
            cnt[1] += 1
        elif word.isdigit():
            cnt[2] += 1
        else:
            cnt[3] += 1
    print(cnt[0], cnt[1], cnt[2], cnt[3]-1)
