from collections import deque
import sys

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    indegree[b] += 1
start, end = map(int, input().rstrip().split())
INF = int(1e9)
time = [0]*(n+1)
cnt = [0]*(n+1)
q = deque()
q.append(start)
for i in range(1, n+1):
    if i == start:
        continue
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        next, cost = i
        if time[next] <= time[now] + cost:
            if time[next] < time[now] + cost:
                if next == end:
                    cnt[next] = cnt[now]+ 1
                else:
                    cnt[next] = 1
                time[next] = time[now]+cost
            else:
                if next == end:
                    cnt[next] += (cnt[now] + 1)
                else:
                    cnt[next] += 1
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)


print(time[end])
print(cnt[end])