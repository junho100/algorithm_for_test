import sys

input = sys.stdin.readline

N = int(input().rstrip())
k = int(input().rstrip())

start = 1
end = min(10**9, N*N)
result = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in range(1, N+1):
        tmp += min(mid//i, N)
    
    if tmp >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)