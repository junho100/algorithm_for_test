import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())

        graph[y][x] = 1
    
    def dfs(x, y):
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 1:
                dfs(nx, ny)
        
        return 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                result += dfs(i, j)
    
    print(result)