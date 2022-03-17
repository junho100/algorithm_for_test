from collections import deque
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
T = int(input().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[0]*(M) for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().rstrip().split())
        graph[b][a] = 1
    
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    def bfs(x, y):
        q = deque()
        visited[x][y] = True
        q.append([x, y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    def dfs(x, y):
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)

