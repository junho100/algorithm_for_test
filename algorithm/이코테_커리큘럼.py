from collections import deque
import copy

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
time = [0]*(N+1)
for i in range(1, N+1):
    d = list(map(int, input().split()))

    time[i] = d[0]
    needs = d[1:-1]

    for j in range(len(needs)):
        graph[needs[j]].append(i)
        indegree[i] += 1
total = copy.deepcopy(time)
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        total[i] = max(total[i], total[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(total[i])