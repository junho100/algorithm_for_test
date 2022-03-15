import sys

input = sys.stdin.readline

N = int(input().rstrip())

a = [False, False] + [True] * (N-1)
nums = []

for i in range(2, N+1):
    if a[i]:
        nums.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

s = []
tmp = 0
for num in nums:
    tmp += num
    s.append(tmp)

start = 0
end = 0
result = 0
while start <= end and end < len(nums):
    left = start -1
    right = end

    t = 0
    if left < 0:
        t = s[right]
    else:
        t = s[right] - s[left]

    if t == N:
        result += 1
        end += 1
    elif t < N:
        end += 1
    else:
        start += 1

print(result)