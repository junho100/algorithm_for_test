import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

visited = [[False]*C for _ in range(R)]

s = [False]*(ord("Z") - ord("A") + 1)
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global result
    check = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if not visited[nx][ny]:
            if s[ord(graph[nx][ny]) - ord("A")]:
                if not check:
                    check =True
                    m = s.count(True)
                    if result < m:
                        result = m
            else:
                visited[nx][ny] = True
                s[ord(graph[nx][ny]) - ord("A")] = True
                dfs(nx, ny)
                visited[nx][ny] = False
                s[ord(graph[nx][ny]) - ord("A")] = False

s[ord(graph[0][0]) - ord("A")] = True
visited[0][0] = True
dfs(0, 0)
print(result)