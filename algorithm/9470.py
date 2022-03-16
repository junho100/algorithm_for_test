from collections import deque
import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    K, M, P = map(int, input().rstrip().split())

    graph = [[] for _ in range(M+1)]
    indegree = [0]*(M+1)

    for _ in range(P):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1
    
    q = deque()
    s = [0]*(M+1)
    cnt = [0]*(M+1)
    s_max = [0]*(M+1)
    for i in range(1, M+1):
        if indegree[i] == 0:
            q.append(i)
            s[i] = 1
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            if s_max[i] == s[now]:
                cnt[i] += 1
            elif s_max[i] < s[now]:
                cnt[i] = 1
                s_max[i] = s[now]
            indegree[i] -= 1

            if indegree[i] == 0:
                if cnt[i] == 1:
                    s[i] = s_max[i]
                elif cnt[i] >= 2:
                    s[i] = s_max[i] + 1
                q.append(i)
    print(K, s[M])