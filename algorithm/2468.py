import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input().rstrip())
visited = [[False] * N for _ in range(N)]
graph = []
m = 100
for i in range(N):
    d = list(map(int, input().rstrip().split()))
    graph.append(d)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, graph, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if not visited[nx][ny] and graph[nx][ny] != 0:
            visited = dfs(nx, ny, graph, visited)
    return visited

result = 1
for k in range(1, m+1):
    graph_copy = copy.deepcopy(graph)
    visited_copy = copy.deepcopy(visited)
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] <= k:
                graph_copy[i][j] = 0
                visited_copy[i][j] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited_copy[i][j]:
                visited_copy = dfs(i, j, graph_copy, visited_copy)
                cnt += 1
    result = max(result, cnt)
print(result)