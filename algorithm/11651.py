N = int(input())
loc = []

for _ in range(N):
    x, y = map(int, input().split())

    loc.append((x, y))

loc.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(loc[i][0], loc[i][1])