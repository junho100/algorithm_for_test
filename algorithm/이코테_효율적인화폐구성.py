N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
INF = int(1e9)
d = [INF]*(10001)

for i in coins:
    d[i] = 1

for i in coins:
    for j in range(i, M+1):
        d[j] = min(d[j], d[j-i] + 1)

if d[M] >= INF:
    print(-1)
else:
    print(d[M])