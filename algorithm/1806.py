import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())

nums = list(map(int, input().rstrip().split()))
d = []
s = 0
for num in nums:
    s += num
    d.append(s)
start = 0
end = 1
INF = int(1e9)
result = INF
while start < end and end <= N:
    if end-start >= result:
        start += 1
        continue
    s = 0
    left = start -1
    right = end - 1
    if left < 0:
        s = d[right]
    else:
        s = d[right] - d[left]

    if s < S:
        end += 1
    else:
        result = min(end-start, result)
        start += 1

if result >= INF:
    print(0)
else:
    print(result)