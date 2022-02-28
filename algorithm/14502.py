from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

total = []
viruses = []
for i in range(N):
    for j in range(M):
        total.append([i, j])
        if graph[i][j] == 2:
            viruses.append([i, j])



cans = list(combinations(total, 3))
result = 0
dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]
for can in cans:
    visited = [[False]*(M) for _ in range(N)]
    def bfs(x, y):
        visited[x][y] = True
        q = deque()
        q.append([x, y])

        while q:
            now = q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if (not visited[nx][ny]) and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])

    if graph[can[0][0]][can[0][1]] != 0 or graph[can[1][0]][can[1][1]] != 0 or graph[can[2][0]][can[2][1]] != 0:
        continue
    for i in range(3):
        graph[can[i][0]][can[i][1]] = 1
    
    for i in range(len(viruses)):
        x, y = viruses[i]

        if not visited[x][y]:
            bfs(x, y)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and (not visited[i][j]):
                cnt += 1
    result = max(cnt, result)

    for i in range(3):
        graph[can[i][0]][can[i][1]] = 0

print(result)
        
    