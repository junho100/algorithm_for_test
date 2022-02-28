from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

cnt_normal = 0
cnt_dis = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
words = ["R", "G", "B"]

for i in range(2):
    visited = [[False]*N for _ in range(N)]
    def bfs(x, y):
        q = deque()
        visited[x][y] = True
        q.append((x, y))
        target = graph[x][y]
        while q:
            now = q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if (not visited[nx][ny]) and graph[nx][ny] == target:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    def bfs_dis(x, y):
        q = deque()
        visited[x][y] = True
        q.append((x, y))
        target = graph[x][y]
        while q:
            now = q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                
                if (not visited[nx][ny]):
                    if target in ["R", "G"]:
                        if graph[nx][ny] in ["R", "G"]:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                    else:
                        if target == graph[nx][ny]:
                            visited[nx][ny] = True
                            q.append([nx, ny])
    if i == 0:
        for i in range(N):
            for j in range(N):
                if graph[i][j] in words and (not visited[i][j]):
                    bfs(i, j)
                    cnt_normal += 1
    elif i == 1:
        for i in range(N):
            for j in range(N):
                if graph[i][j] in words and (not visited[i][j]):
                    bfs_dis(i, j)
                    cnt_dis += 1
print(cnt_normal, cnt_dis)
