import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + 1

                if distance[i] > cost:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))
    dijkstra(1)
    for i in range(1, n+1):
        if distance[i] >= INF:
            distance[i] = -1
    m = max(distance[1:])
    print(distance)
    for i in range(1, n+1):
        if distance[i] == m:
            answer += 1


    return answer
