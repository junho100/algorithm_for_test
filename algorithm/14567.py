from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

distance = [1]*(N+1)

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        distance[i] = max(distance[i], distance[now]+1)
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*distance[1:])