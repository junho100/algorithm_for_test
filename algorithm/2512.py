import sys

input = sys.stdin.readline

N = int(input().rstrip())
cashes = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
s_cash = sum(cashes)
start = 1
end = max(cashes)

if s_cash <= M:
    print(end)
    exit()
result = 0
while start <= end:
    mid = (start + end) // 2

    s = 0

    for cash in cashes:
        if cash > mid:
            s += mid
        else:
            s += cash
    
    if s > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)