import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input().rstrip())
def dfs(start, g):
    group[start] = g

    for i in graph[start]:
        if group[i] == 0:
            a = dfs(i, -g)
            if not a:
                return False
        else:
            if group[start] == group[i]:
                return False
    return True
for _ in range(K):
    V, E = map(int, input().rstrip().split())
    group = [0]*(V+1)
    graph = [[]for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if group[i] == 0:
            tmp = dfs(i, -1)
            if not tmp:
                print("NO")
                break
    else:
        print("YES")