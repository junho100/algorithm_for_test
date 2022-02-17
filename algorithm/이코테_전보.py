import heapq

N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[0]

            if cost < distance[i[1]]:
                distance[i[1]] = cost

                heapq.heappush(q, (cost, i[1]))

dijkstra(C)
m = 0
cnt = 0
for i in range(1, N+1):
    if distance[i] not in [INF, 0]:
        cnt += 1
        m = max(m, distance[i])

print(cnt, m)