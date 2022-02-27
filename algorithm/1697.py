import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
INF = int(1e9)
d = [INF]*(100001)
d[N] = 0

for i in range(K+1):
    if K == N:
        break
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i >= 1:
        d[i] = min(d[i], d[i-1] + 1)
    d[i] = min(d[i], d[i+1] + 1)

print(d[K])