from collections import deque
import sys

input = sys.stdin.readline
N, L, R = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
def bfs(x, y):
    tmp = []
    q = deque()
    q.append([x,y])
    tmp.append([x, y])
    visited[x][y] = True

    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if not visited[nx][ny] and (L <= abs(graph[x][y] - graph[nx][ny]) <= R):
                q.append([nx, ny])
                visited[nx][ny] = True
                tmp.append([nx, ny])
    return tmp
while True:
    visited = [[False]*N for _ in range(N)]

    check = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tmp = bfs(i, j)

                if len(tmp) > 1:
                    check = True
                    s = 0
                    for x, y in tmp:
                        s += graph[x][y]
                    else:
                        s = s // len(tmp)
                    for x, y in tmp:
                        graph[x][y] = s
    if not check:
        break
    else:
        cnt += 1
print(cnt)