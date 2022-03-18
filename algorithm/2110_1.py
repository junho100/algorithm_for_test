import sys

input = sys.stdin.readline

N , C = map(int, input().rstrip().split())
houses = []

for _ in range(N):
    houses.append(int(input().rstrip()))

houses.sort()
result = 0
start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    current = houses[0]
    for i in range(1, N):
        if (houses[i] - current) >= mid:
            cnt += 1
            current = houses[i]
    
    if cnt < C:
        end = mid-1
    else:
        result = max(result, mid)
        start = mid + 1

print(result)
