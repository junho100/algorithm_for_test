import sys

input = sys.stdin.readline

N = int(input().rstrip())
INF = int(1e9)
d = [INF]*(1000001)
d[1] = 0
d[2] = 1
d[3] = 1
results = [[] for _ in range(1000001)]
results[1].append(1)
for i in range(2, 4):
    results[i].append(1)
    results[i].append(i)
for i in range(4, N+1):
    if d[i] > (d[i-1] + 1):
        d[i] = d[i-1] + 1
    results[i] = results[i-1] + [i]
    if i % 2 == 0:
        if d[i] > (d[i//2] + 1):
            d[i] = d[i//2] + 1
            results[i] = results[i // 2] + [i]
    if i % 3 == 0:
        if d[i] > (d[i//3] + 1):
            d[i] = d[i//3] + 1
            results[i]= results[i//3] + [i]

print(d[N])
results[N].sort( reverse = True)
for i in range(len(results[N])):
    print(results[N][i], end = " ")