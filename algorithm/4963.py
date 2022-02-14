import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        exit()
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    def dfs(x, y):
        graph[x][y] = 0

        for i in range(8):
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