import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
result = 0
def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    
    return 1

for i in range(1, N+1):
    if not visited[i]:
        result += dfs(i)

print(result)