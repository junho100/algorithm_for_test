import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for tree in trees:
        if mid < tree:
            total += (tree-mid)
    
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)