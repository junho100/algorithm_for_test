import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

start = 0
end = 1
result = int(1e9)
sub_sum = []
tmp = 0
for num in nums:
    tmp += num
    sub_sum.append(tmp)
while start < end and (end <= N):
    s = 0
    if start == 0:
        s = sub_sum[end-1]
    else:
        s = sub_sum[end-1] - sub_sum[start-1]

    if s >= S:
        result = min(result, end-start)
        start += 1
    else:
        end += 1

if result >= int(1e9):
    print(0)
else:
    print(result)
