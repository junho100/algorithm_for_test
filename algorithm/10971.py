import sys

input = sys.stdin.readline

N = int(input().rstrip())
s = 0
visited = [False]*(N)
graph = []
distance = [[int(1e9)]*N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

def dfs(now,cnt, start):
    global s
    if cnt == (N):
        distance[start][now] = min(distance[start][now], s)
        return
    
    for i in range(N):
        if (not visited[i]) and (graph[now][i] != 0):
            visited[i] = True
            s += graph[now][i]
            dfs(i, cnt + 1, start)
            s -= graph[now][i]
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i, 1, i)
    visited[i] = False

result = int(1e9)

for i in range(N):
    for j in range(N):
        if i != j and graph[j][i] != 0:
            result = min(result, distance[i][j] + graph[j][i])
            
print(result)