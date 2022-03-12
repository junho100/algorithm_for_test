import heapq
import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    n, m, t = map(int, input().rstrip().split())
    s, g, h = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        if (a == g and b == h) or (a == h and b == g):
            graph[a].append((b, -c))
            graph[b].append((a, -c))
        else:
            graph[a].append((b, c))
            graph[b].append((a, c))
        
    INF = int(1e9)
    distance = [INF]*(n+1)

    cans = []
    isCross = [False]*(n+1)
    for _ in range(t):
        c = int(input().rstrip())
        cans.append(c)
    
    def dijkstra(start):
        q = []
        distance[start] = 0

        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = 0
                tmp = False
                if i[1] < 0:
                    cost = dist - i[1]
                    tmp = True
                else:
                    cost = dist + i[1]
                if distance[i[0]] >= cost:
                    if tmp or (isCross[now] == True):
                        isCross[i[0]] = True
                    if distance[i[0]] > cost:
                        if not (tmp or (isCross[now] == True)):
                            isCross[i[0]] = False
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))
    dijkstra(s)
    cans.sort()
    for can in cans:
        if isCross[can]:
            print(can, end = " ")
    print()