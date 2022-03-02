import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
INF = max(N, K)
distance = [INF]*(100001)

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        if now*2 <= 100000:
            cost = dist
            if distance[now*2] > cost:
                distance[now*2] = cost
                heapq.heappush(q, (cost, now*2))
        if now >= 1:
            cost = dist + 1
            if distance[now-1] > cost:
                distance[now-1] = cost
                heapq.heappush(q, (cost, now-1))
        if now < 100000:
            cost = dist + 1
            if distance[now+1] > cost:
                distance[now+1] = cost
                heapq.heappush(q, (cost, now+1))
dijkstra(N)
print(distance[K])