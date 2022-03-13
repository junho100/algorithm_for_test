import sys

input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

current = int(y*100/x)

start = 1
end = 10**9
result = 0
while start <= end:
    mid = (start + end) // 2

    nx = x + mid
    ny = y + mid

    tmp = int(ny*100/nx)

    if tmp == current:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

if result == 0:
    print(-1)
else:
    print(result)