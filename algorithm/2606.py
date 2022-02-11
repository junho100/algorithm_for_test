from collections import deque

N = int(input())
M= int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [False]*(N+1)
q.append(1)
visited[1] = True

while q:
    a = q.popleft()

    for i in graph[a]:
        if not visited[i]:
            visited[i] = True
            q.append(i)

print(visited.count(True)-1)
