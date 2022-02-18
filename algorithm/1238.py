import heapq
import copy
import sys

input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = []
INF = int(1e9)
distance = [INF]*(N+1)
distance_copy = copy.deepcopy(distance)
def dijkstra(start, distance):
    q = []
    distance[start] = 0

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

dijkstra(X, distance_copy)
for i in range(1, N+1):
    result.append(distance_copy[i])
    distance = [INF]*(N+1)
    dijkstra(i, distance)
    result[i-1] += distance[X]

print(max(result))