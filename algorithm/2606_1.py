from collections import deque
import sys

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
cnt = 0

def bfs(x):
    global cnt
    q = deque()
    visited[x] = True
    q.append(x)

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

def dfs(x):
    global cnt
    visited[x] = True
    cnt += 1

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(cnt-1)