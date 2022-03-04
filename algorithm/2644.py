import sys

input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().rstrip().split())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]
distance = [n+1]*(n+1)
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().rstrip().split())

    graph[y].append(x)
    graph[x].append(y)
start = 0
def dfs(x, start):
    visited[x] = True
    distance[x] = start
    for i in graph[x]:
        if not visited[i]:
            dfs(i, start + 1)
dfs(a, start)

if distance[b] == n+1:
    print(-1)
else:
    print(distance[b])