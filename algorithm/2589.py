from collections import deque
import sys

input = sys.stdin.readline
N ,M = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
def bfs(x, y):
    global result
    q = deque()
    visited[x][y] = True
    q.append([x, y, 0])

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if not visited[nx][ny] and graph[nx][ny] == "L":
                q.append((nx, ny, now[2]+1))
                visited[nx][ny] = True
                result = max(result, now[2]+1)

for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            visited = [[False]*M for _ in range(N)]
            bfs(i, j)
print(result)