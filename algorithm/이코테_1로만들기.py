X = int(input())
INF = int(1e9)
d = [INF]*(30001)
d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 1

for i in range(6, X+1):
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
    d[i] = min(d[i], d[i-1] + 1)
print(d[X])
