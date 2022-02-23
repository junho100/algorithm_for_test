N, M = map(int, input().split())

rices = list(map(int, input().split()))

start = 0
end = max(rices)
result = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for rice in rices:
        if mid < rice:
            cnt += rice - mid
    if cnt < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)