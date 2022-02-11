from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs_result = []
def dfs(start, visited):
    visited[start] = True
    dfs_result.append(start)
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited)
bfs_result = []
def bfs(start, visited):
    q = deque()
    q.append(start)
    bfs_result.append(start)
    visited[start] = True

    while q:
        a = q.popleft()

        for i in graph[a]:
            if not visited[i]:
                bfs_result.append(i)
                q.append(i)
                visited[i] = True
visited = [False]*(N+1)
dfs(V, visited)
visited = [False]*(N+1)
bfs(V, visited)

for i in range(len(dfs_result) - 1):
    print(dfs_result[i], end =" ")
else:
    print(dfs_result[len(dfs_result) - 1])
for i in range(len(bfs_result) - 1):
    print(bfs_result[i], end =" ")
else:
    print(bfs_result[len(bfs_result) - 1])
