import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input().rstrip())
visited = [False] * (N+1)
parent = [1]*(N+1)
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())

    graph[b].append(a)
    graph[a].append(b)

def dfs(now):
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            parent[i] = now
            dfs(i)
dfs(1)
for i in range(2, N+1):
    print(parent[i])