import sys
import heapq
input = sys.stdin.readline

N ,E = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())

    graph[b].append((c, a))
    graph[a].append((c, b))
v1, v2 = map(int, input().rstrip().split())
t1 = 0
t2 = 0
for i in range(3):
    distance = [INF]*(N+1)

    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[0]

                if distance[i[1]] > cost:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))
    
    if i == 0:
        dijkstra(1)
        t1 += distance[v1]
        t2 += distance[v2]
    elif i == 1:
        dijkstra(v1)
        t1 += distance[v2]
        t2 += distance[N]
    elif i == 2:
        dijkstra(v2)
        t1 += distance[N]
        t2 += distance[v1]

result = min(t1, t2)
if result >= INF:
    print(-1)
else:
    print(result)