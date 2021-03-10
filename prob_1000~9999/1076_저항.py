import sys
input = sys.stdin.readline

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
mul = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

s = ''
result = 0
a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

s = int(str(color.index(a)) + str(color.index(b)))
result = s * mul[color.index(c)]

print(result)
