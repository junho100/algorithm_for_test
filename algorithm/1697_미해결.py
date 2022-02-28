import sys

input = sys.stdin.readline

from collections import deque

N, K = map(int, input().rstrip().split())

visited = [False]*(100002)
d = [0]*(100002)

def bfs(start):
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        now = q.popleft()

        if now*2 < 100000 and now*2 >= 1:
            if not visited[now*2]:
                visited[now*2] = True
                d[now*2] = d[now] + 1
                q.append(now*2)
        if now >= 1:
            if not visited[now-1]:
                visited[now - 1] = True
                d[now-1] = d[now] + 1
                q.append(now-1)
        if now <= 100000:
            if not visited[now + 1]:
                visited[now + 1] = True
                d[now + 1] = d[now] + 1
                q.append(now + 1)
bfs(N)
print(d[K])