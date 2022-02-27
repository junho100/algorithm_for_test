import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
m = max(map(max, graph))
s = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def dfs(x, y):
    global result
    if len(s) < 4:
        tmp = 0
        for i in range(len(s)):
            tmp += graph[s[i][0]][s[i][1]]
        if result >= tmp + m * (4-len(s)):
            return
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
            if len(s) == 2:
                s.append([nx, ny])
                dfs(x, y)
                s.pop()
            s.append([nx, ny])
            dfs(nx, ny)
            s.pop()
            
    

for i in range(N):
    for j in range(M):
        s.append([i, j])
        dfs(i, j)
        s.pop()
print(result)