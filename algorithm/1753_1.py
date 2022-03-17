import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().rstrip().split())

graph = [[] for _ in range(V+1)]
INF = int(1e9)
distance = [INF]*(V+1)
s = int(input().rstrip())
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([c, b])

def dijkstra(start):
    distance[start] = 0
    q = []

    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            cost = distance[now] + i[0]

            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(s)

for i in range(1, V+1):
    if distance[i] >= INF:
        print("INF")
    else:
        print(distance[i])