import sys

input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
lines = []
for _ in range(K):
    lines.append(int(input().rstrip()))

result = 0

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for line in lines:
        cnt += (line // mid)
    
    if cnt < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)