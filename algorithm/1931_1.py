import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = []
cnt = 0
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    arr.append([a, b])

arr.sort(key = lambda x : (x[1], x[0]))
tmp = 0
for i in arr:
    start, end = i

    if tmp <= start:
        cnt += 1
        tmp = end

print(cnt)