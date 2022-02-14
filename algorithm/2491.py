N = int(input())
nums = list(map(int, input().split()))

d = [0]*(100001)

cnt = 1
d[0] = 1
for i in range(1, N):
    if nums[i-1] <= nums[i]:
        cnt += 1
    else:
        cnt = 1
    d[i] = max(d[i-1], cnt)
cnt = 1
for i in range(1, N):
    if nums[i-1] >= nums[i]:
        cnt += 1
    else:
        cnt = 1
    d[i] = max(d[i-1], cnt, d[i])

print(d[N-1])