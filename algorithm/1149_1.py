import sys

input = sys.stdin.readline

N = int(input().rstrip())
houses = []

for _ in range(N):
    houses.append(list(map(int, input().rstrip().split())))

d = [[0,0,0] for _ in range(N)]

for i in range(3):
    d[0][i] = houses[0][i]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            d[i][j] = min(d[i-1][1]+houses[i][j], d[i-1][2] + houses[i][j])
        elif j == 1:
            d[i][j] = min(d[i-1][0]+houses[i][j], d[i-1][2] + houses[i][j])
        else:
            d[i][j] = min(d[i-1][0]+houses[i][j], d[i-1][1] + houses[i][j])

print(min(d[N-1]))