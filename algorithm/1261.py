import heapq

M, N = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    graph.append(list(map(int, list(input()))))
INF = int(1e9)
distance = [[INF]*(M) for _ in range(N)]

def dijkstra(x, y):
    distance[x][y] = 0
    q = []
    heapq.heappush(q, (0, (x, y)))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now[0]][now[1]] < dist:
            continue

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            cost = dist
            if graph[nx][ny] == 1:
                cost += 1

            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))
            
dijkstra(0, 0)

print(distance[N-1][M-1])