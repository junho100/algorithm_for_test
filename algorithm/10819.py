from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

cans = list(permutations(nums, N))

result = 0
for can in cans:
    tmp = 0
    for i in range(1, N):
        tmp += abs(can[i-1] - can[i])
    if tmp > result:
        result = tmp

print(result)
