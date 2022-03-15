n = int(input())
nums = list(map(int,input().split()))
x = int(input())

nums.sort()

start = 0
end = n-1
cnt = 0
while start < end:
    s = nums[start] + nums[end]

    if s < x:
        start += 1
    elif s > x:
        end -= 1
    else:
        cnt += 1
        end -= 1

print(cnt)