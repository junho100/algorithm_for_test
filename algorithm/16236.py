import heapq
import sys

input = sys.stdin.readline
N = int(input().rstrip())
INF = int(1e9)
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
size = 2
eat = 0
result = 0
check = True
x = 0
y = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x = i
            y = j
            graph[i][j] = 0
            break

while check:
    distance = [[INF]*N for _ in range(N)]

    def dijkstra(x, y, size):
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

                if nx < 0 or ny < 0 or nx>= N or ny >= N:
                    continue

                if size < graph[nx][ny]:
                    continue
                
                cost = dist + 1
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))

    dijkstra(x, y, size)
    ds = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] in [1,2,3,4,5,6] and size > graph[i][j] and distance[i][j] < INF:
                ds.append((distance[i][j], i, j))
    if len(ds) == 0:
        check = False
        continue
    ds.sort(key = lambda x : (x[0], x[1], x[2]))
    eat_target = ds[0]
    result += eat_target[0]
    graph[eat_target[1]][eat_target[2]] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    x = eat_target[1]
    y = eat_target[2]
print(result)