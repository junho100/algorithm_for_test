N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

results = []

def dfs(x, y, num):
    graph[x][y] = num
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny, num)
    
    for i in range(N):
        cnt += graph[i].count(num)
    return cnt

num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            results.append(dfs(i, j, num))
            num += 1
results.sort()

print(len(results))
for i in range(len(results)):
    print(results[i])