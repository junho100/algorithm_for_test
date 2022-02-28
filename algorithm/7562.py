from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input().rstrip())

for _ in range(T):
    I = int(input().rstrip())
    x, y = map(int, input().rstrip().split())
    target_x, target_y = map(int, input().rstrip().split())

    visited = [[False]*I for _ in range(I)]
    distance = [[0]*I for _ in range(I)]
    def bfs(x, y):
        visited[x][y] = True
        q = deque()
        q.append([x, y])

        while q:
            now = q.popleft()

            for i in range(8):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= I or ny >= I:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    distance[nx][ny] = distance[now[0]][now[1]]+1
    bfs(x, y)
    print(distance[target_x][target_y])