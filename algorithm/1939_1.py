import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [0]*(N+1)
start, end = map(int, input().rstrip().split())
INF = int(1e9)
def bfs(x):
    q = []
    heapq.heappush(q, (-INF, x))
    distance[x] = INF

    while q:
        now_cost, now = heapq.heappop(q)
        now_cost *= (-1)

        if distance[now] > now_cost:
            continue
        for i in graph[now]:
            next, cost = i
            tmp = min(now_cost, cost)
            if distance[next] < tmp:
                distance[next] = tmp
                heapq.heappush(q, (-tmp, next))

bfs(start)

print(distance[end])