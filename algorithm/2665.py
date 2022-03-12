import heapq
import sys

input = sys.stdin.readline
N = int(input().rstrip())
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

INF = int(1e9)
distance = [[INF]*(N) for _ in range(N)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def dijkstra(x, y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q, (0, (x, y)))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now[0]][now[1]] < dist:
            continue

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            cost = 0
            if graph[nx][ny] == 0:
                cost = distance[now[0]][now[1]] + 1
            else:
                cost = distance[now[0]][now[1]]

            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

dijkstra(0, 0)

print(distance[N-1][N-1])
            