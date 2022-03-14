from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
N ,M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

groups = []

idx = 0
visited = [[False]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, idx):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    groups.append([[x, y]])
    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or ny < 0 or nx >=N or ny >= M:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx, ny])
                groups[idx].append([nx, ny])

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j, idx)
            idx += 1

parent = [i for i in range(idx)]

cans = list(combinations(parent, 2))
INF = int(1e9)

edges = []
def cul_distance(l, r, op):
    cnt = 0
    if op == 0: # horizontal
        if l[1] > r[1]:
            for i in range(r[1]+1, l[1]):
                if graph[l[0]][i] == 0:
                    cnt += 1
                else:
                    cnt = 0
                    break
        else:
            for i in range(l[1]+1, r[1]):
                if graph[l[0]][i] == 0:
                    cnt += 1
                else:
                    cnt = 0
                    break
    elif op == 1: #vertical
        if l[0] > r[0]:
            for i in range(r[0]+1, l[0]):
                if graph[i][l[1]] == 0:
                    cnt += 1
                else:
                    cnt = 0
                    break
        else:
            for i in range(l[0]+1, r[0]):
                if graph[i][l[1]] == 0:
                    cnt += 1
                else:
                    cnt = 0
                    break
    return cnt
for can in cans:
    lefts, rights = can
    d = INF
    for left in groups[lefts]:
        for right in groups[rights]:
            if left[0] == right[0]:
                tmp = cul_distance(left, right, 0)
                if tmp >= 2:
                    d = min(d, tmp)
            elif left[1] == right[1]:
                tmp = cul_distance(left, right, 1)
                if tmp >= 2:
                    d = min(d, tmp)
    if d < INF:
        edges.append((d, lefts, rights))

edges.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y: 
        parent[y] = x
    else:
        parent[x] = y
result = 0
for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y):
        union(x, y)
        result += cost
check = True
for i in range(1, idx):
    if find_parent(i-1) != find_parent(i):
        check = False
        break
if check:
    print(result)
else:
    print(-1)