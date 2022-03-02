import heapq
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
while True:
    N = int(input().rstrip())
    if N == 0:
        break

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().rstrip().split())))
    INF = int(1e9)
    distance = [[INF]*N for _ in range(N)]

    def dijkstra(x, y):
        distance[x][y] = graph[x][y]
        q = []
        heapq.heappush(q, (distance[x][y], (x, y)))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now[0]][now[1]] < dist:
                continue

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                cost = dist + graph[nx][ny]

                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
    dijkstra(0, 0)
    cnt += 1
    print("Problem",str(cnt) + ":", distance[N-1][N-1])
