import sys

input = sys.stdin.readline

d = list(map(int, input().rstrip().split()))

N = d[0]
a = d[1]
b = d[2]
cnt = 0

while a != b:
    a -= a//2
    b -= b // 2
    cnt += 1
print(cnt)