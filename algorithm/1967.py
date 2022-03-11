import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start):
    for i in graph[start]:
        if distance[i[0]] == -1:
            distance[i[0]] = distance[start] + i[1]
            dfs(i[0])

distance = [-1]*(N+1)
distance[1] = 0
dfs(1)

start = distance.index(max(distance))
distance = [-1]*(N+1)
distance[start] = 0
dfs(start)
print(max(distance))