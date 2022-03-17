import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

d = [1]*(N)

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))