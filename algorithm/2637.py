from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    for _ in range(c):
        graph[b].append(a)
        indegree[a] += 1

primary = []
primary_idx = dict()
idx = 0
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        primary.append(i)
        primary_idx[i] = idx
        idx += 1

needs = [[0]*len(primary) for _ in range(N+1)]
for i in primary:
    needs[i][primary_idx[i]] = 1

while q:
    now = q.popleft()

    for i in graph[now]:
        for j in range(len(primary)):
            needs[i][j] += needs[now][j]
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)


for i in range(len(primary)):
    print(primary[i], needs[N][i] )