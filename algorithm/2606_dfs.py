N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


visited = [False]*(N+1)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True)-1)