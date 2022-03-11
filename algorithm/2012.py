N = int(input())
result = 0
nums = []
for i in range(1, N+1):
    nums.append(int(input()))

nums.sort()

for i in range(1, N+1):
    result += abs(nums[i-1] - i)
print(result)