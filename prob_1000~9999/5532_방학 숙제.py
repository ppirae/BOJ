L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
korean = 0
math = 0

if A%C == 0:
    korean = A//C
else:
    korean = int(A/C) + 1

if B%D == 0:
    math = B//D
else:
    math = int(B/D) + 1

if korean > math:
    print(L-korean)
else:
    print(L-math)
