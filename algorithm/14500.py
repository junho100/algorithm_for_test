import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N, M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

s = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def dfs(x, y):
    global result
    if len(s) == 4:
        tmp = 0
        for i in range(4):
            tmp += graph[s[i][0]][s[i][1]]
        result = max(result, tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if [nx, ny] not in s:
            s.append([nx, ny])
            dfs(nx,ny)
            s.pop()
        else:
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        dfs(i, j)
print(result)