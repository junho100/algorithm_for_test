import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums_copy = sorted(list(set(nums)))

dic = {nums_copy[i] : i for i in range(len(nums_copy))}

for i in range(N):
    print(dic[nums[i]], end = " ")
