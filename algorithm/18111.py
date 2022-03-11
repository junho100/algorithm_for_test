import sys

input = sys.stdin.readline
N ,M, B = map(int, input().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

t = int(1e9)
h = 0

for k in range(256, -1, -1):
    B_tmp = B
    time = 0
    c = True
    for i in range(N):
        if not c:
            break
        for j in range(M):
            if graph[i][j] > k:
                B_tmp += (graph[i][j] - k)
                time += (2*(graph[i][j] - k))
            else:
                B_tmp -= (k - graph[i][j])
                time += (k - graph[i][j])
            if time >= t:
                c = False
                break

    if B_tmp >= 0 and c:
        if t > time:
            t = time
            h = k
    else:
        continue
print(t, h)