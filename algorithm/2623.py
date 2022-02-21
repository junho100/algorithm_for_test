from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
result = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    d = tmp[1:]
    for i in range(1, len(d)):
        if d[i] not in graph[d[i-1]]:
            graph[d[i-1]].append(d[i])
            indegree[d[i]] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != N:
    print(0)
else:
    for i in range(N):
        print(result[i])