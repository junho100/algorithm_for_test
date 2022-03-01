import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
x, y, d = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

visited = [[False]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def change_d(d):
    d -= 1
    if d == -1:
        return 3
    else:
        return d
cnt = 0
while True:
    if not visited[x][y]:   
        visited[x][y] = True
        cnt += 1

    for i in range(4):
        d = change_d(d)
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if graph[nx][ny] == 1 or visited[nx][ny] == True:
            continue

        x = nx
        y = ny
        break
    else:
        d = change_d(d)
        d = change_d(d)
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            print(cnt)
            break
            
        if graph[nx][ny] == 1:
            print(cnt)
            break
        x = nx
        y = ny
        d = change_d(d)
        d = change_d(d)

