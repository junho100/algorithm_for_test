import sys

input = sys.stdin.readline

N = int(input().rstrip())
prices = [0]
tmp = list(map(int, input().rstrip().split()))
prices += tmp
INF = int(1e9)
d = [INF]*(1001)
for i in range(1, N+1):
    d[i] = prices[i]

for i in range(1, N+1):
    for j in range(i+1, N+1):
        d[j] = min(d[j], d[j-i]+prices[i])
print(d[N])