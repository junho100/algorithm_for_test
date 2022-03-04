from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

visited = [[False]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    cnt = 1

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue

            if not visited[nx][ny] and (graph[nx][ny] == 1):
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    return cnt
cans = []
for i in range(N):
    for j in range(M):
        if (not visited[i][j]) and graph[i][j] == 1:
            tmp = bfs(i, j)
            cans.append(tmp)
print(len(cans))
if len(cans) == 0:
    print(0)
else:
    print(max(cans))