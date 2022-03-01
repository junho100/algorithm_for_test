from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split())

graph = [[0]*N for _ in range(M)]

for _ in range(K):
    y_1, x_1, y_2, x_2 = map(int, input().rstrip().split())
    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            graph[i][j] = 1
visited = [[False]*N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append([x, y])
    cnt = 1
    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[nx][ny] == 0 and (not visited[nx][ny]):
                cnt += 1
                q.append([nx, ny])
                visited[nx][ny] = True
    return cnt
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and (not visited[i][j]):
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i, end = " ")