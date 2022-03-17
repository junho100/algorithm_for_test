from collections import deque
import sys

input = sys.stdin.readline
N = int(input().rstrip())
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    result.append(1)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>= N or ny >= N:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True
                result[-1]+= 1

def dfs(x, y, idx):
    visited[x][y] = True
    result[idx] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >=N:
            continue

        if not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny, idx)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            result.append(0)
            dfs(i, j, len(result)-1)

result.sort()
print(len(result))
for i in result:
    print(i)

