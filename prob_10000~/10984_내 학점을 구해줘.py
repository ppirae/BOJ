t = int(input())
for i in range(t):
    n = int(input())
    total_se = 0
    grade = 0
    total_grade = 0
    for j in range(n):
        a, b = map(float, input().split())
        total_se += a
        grade += b
        total_grade += a*b
    GPA = total_grade/total_se
    print(int(total_se), end = ' ')
    print("%.1f" % GPA)
