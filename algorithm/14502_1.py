from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline
N ,M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

viruses = []
empties = []
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            viruses.append([i,j])
        elif graph[i][j] == 0:
            empties.append([i, j])

cans = list(combinations(empties, 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append([x, y])

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if (not visited[nx][ny]) and (graph[nx][ny] != 1):
                visited[nx][ny] = True
                q.append([nx, ny])
for can in cans:
    visited = [[False]*(M) for _ in range(N)]
    for i in range(3):
        x, y = can[i]
        graph[x][y] = 1
    
    for virus in viruses:
        if not visited[virus[0]][virus[1]]:
            bfs(virus[0], virus[1])

    cnt = 0

    for i in range(N):
        for j in range(M):
            if (not visited[i][j]) and graph[i][j] == 0:
                cnt += 1
    result = max(cnt, result)

    for i in range(3):
        x, y = can[i]
        graph[x][y] = 0

print(result)