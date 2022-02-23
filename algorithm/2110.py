import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
houses = []
for _ in range(N):
    houses.append(int(input().rstrip()))

houses.sort()

start = 1
end = houses[-1]
result = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1

    cur = houses[0]
    for i in range(1, N):
        if (houses[i] - cur) >= mid:
            cnt += 1
            cur = houses[i]

    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
