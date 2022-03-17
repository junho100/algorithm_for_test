from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input().rstrip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

idxs = [i for i in range(N)]

cans = list(combinations(idxs, N//2))
result = int(1e9)

for can in cans:
    a = can
    b = [i for i in idxs if i not in a]

    a_cnt = 0
    b_cnt = 0

    for i in range(len(a)):
        for j in range(len(a)):
            a_cnt += graph[a[i]][a[j]]
            b_cnt += graph[b[i]][b[j]]
    result = min(result, abs(a_cnt - b_cnt))

print(result)