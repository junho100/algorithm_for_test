import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())

roads = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
def dijkstra(start):
    distance[start] = 0
    roads[start].append(start)
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                roads[i[0]] = roads[now] + [i[0]]
dijkstra(start)

print(distance[end])
print(len(roads[end]))
print(*roads[end])