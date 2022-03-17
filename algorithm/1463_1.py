import sys

input = sys.stdin.readline

N = int(input().rstrip())
INF = int(1e9)
d = [INF]*(1000001)
d[3] = 1
d[2] = 1
d[1] = 0

for i in range(4, N+1):
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    d[i] = min(d[i], d[i-1]+1)

print(d[N])
