import math
import sys

input = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(list(input().rstrip()))

K = int(input().rstrip())
moves = []
for _ in range(K):
    moves.append(list(map(int, input().rstrip().split())))
# 1 : right, -1 : left
def rotate(op, target):
    if op == 1:
        last = gears[target][-1]
        gears[target].insert(0, last)
        gears[target] = gears[target][:-1]
    elif op == -1:
        first = gears[target][0]
        gears[target].append(first)
        gears[target] = gears[target][1:]

def solve(op, target, visited):
    visited[target] = True
    if target - 1 >= 0:
        if (gears[target][6] != gears[target-1][2]) and (not visited[target-1]):
            solve(op*(-1), target-1, visited)
    if target + 1 <= 3:
        if (gears[target][2] != gears[target+1][6]) and (not visited[target+1]):
            solve(op*(-1), target+1, visited)
    rotate(op, target)

for move in moves:
    visited = [False]*(4)
    num, op = move

    solve(op, num-1, visited)

result = 0
for i in range(4):
    if gears[i][0] == "1":
        result += int(math.pow(2, i))
print(result)