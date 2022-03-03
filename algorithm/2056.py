from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
times = [0]*(N+1)
d = [0]*(N+1)
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().rstrip().split()))

    times[i] = tmp[0]
    d[i] = tmp[0]

    if tmp[1] == 0:
        continue
    else:
        for j in tmp[2:]:
            graph[j].append(i)
            indegree[i] += 1
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        d[i] = max(d[i], d[now] + times[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(max(d))