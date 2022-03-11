import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    m = 0
    result = 0

    for i in range(N-1, -1, -1):
        if nums[i] > m:
            m = nums[i]
        else:
            result += (m - nums[i])
    print(result)
