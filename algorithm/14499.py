import sys

input = sys.stdin.readline
N, M, x, y, K = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

dice = [0]*6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
ops = list(map(int,input().rstrip().split()))

def change_d(d):
    new_dice = [0]*6
    if d == 1:
        new_dice[0] = dice[3]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
    elif d == 2:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
    elif d == 4:
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
    elif d == 3:
        new_dice[0] = dice[4]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[2]
    return new_dice

for op in ops:
    nx = x + dx[op]
    ny = y + dy[op]

    if nx < 0 or ny < 0 or nx>= N or ny >= M:
        continue
    dice = change_d(op)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[0])
    x = nx
    y = ny
