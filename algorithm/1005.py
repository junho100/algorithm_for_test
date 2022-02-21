from collections import deque
import copy
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0]
    d = list(map(int, input().split()))
    times += d
    dp = copy.deepcopy(times)
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)

    q = deque()

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + times[i])
            if indegree[i] == 0:   
                q.append(i)
    W = int(input())
    print(dp[W])