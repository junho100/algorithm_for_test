from collections import deque

N, M = map(int, input().split())

indegree = [0]*(N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)

q = deque()
result = []
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

for i in range(len(result)):
    print(result[i], end = " ")

