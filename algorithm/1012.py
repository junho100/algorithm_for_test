from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    graph = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())

        graph[b][a] = 1

    def bfs(a, b):
        q = deque()
        q.append((a, b))
        graph[a][b] = 0
        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
        return 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                result += bfs(i, j)

    print(result)