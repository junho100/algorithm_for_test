from collections import deque

N = int(input())
graph = []
for _ in range(N):
    raw = list(map(int, list(input())))

    graph.append(raw)
result = []
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    
    result.append(cnt)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])

