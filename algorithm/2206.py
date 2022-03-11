from collections import deque
import sys

input = sys.stdin.readline
N ,M = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))
INF = int(1e9)
result = INF
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
distance = [[[INF]*2 for _ in range(M)]for _ in range(N)]
distance[0][0][0] = 1
q = deque()
q.append([0, 0, 0])
while q:
    now = q.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if now[2] == 0:
            if graph[nx][ny] == 1 and distance[nx][ny][1] >= INF:
                distance[nx][ny][1] = distance[now[0]][now[1]][now[2]] + 1
                q.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and distance[nx][ny][0] >= INF:
                distance[nx][ny][0] = distance[now[0]][now[1]][now[2]] + 1
                q.append((nx, ny, 0))
                if nx == N-1 and ny == M-1:
                    break
        else:
            if graph[nx][ny] == 0 and distance[nx][ny][1] >= INF:
                distance[nx][ny][1] = distance[now[0]][now[1]][now[2]] + 1
                q.append((nx, ny, 1))
                if nx == N-1 and ny == M-1:
                    break
m = min(distance[N-1][M-1][0], distance[N-1][M-1][1])
if m >= INF:
    print(-1)
else:
    print(m)