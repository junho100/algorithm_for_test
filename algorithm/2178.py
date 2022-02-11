from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    d = list(map(int, list(input())))
    graph.append(d)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a,b, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                if nx == N-1 and ny == M-1:
                    graph[nx][ny] = graph[x][y] + 1
                    print(graph[nx][ny])
                    return
                else:
                    graph[nx][ny] = graph[x][y] + 1

visited = [[False]*(M) for _ in range(N)]
bfs(0, 0, visited)
            
