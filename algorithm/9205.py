import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    ways = []
    for _ in range(n+2):
        ways.append(list(map(int, input().rstrip().split())))
    cnt = 20

    q = deque()
    visited = [False]*(n+2)
    visited[0] = True
    q.append(0)

    while q:
        now = q.popleft()

        for i in range(n+2):
            if i == now:
                continue

            a = abs(ways[now][0] - ways[i][0])
            b = abs(ways[now][1] - ways[i][1])
            if (cnt*(50) >= a+b) and not visited[i]:
                q.append(i)
                visited[i] = True
    if visited[n+1]:
        print("happy")
    else:
        print("sad")