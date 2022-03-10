import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nums = list(map(int, input().rstrip().split()))

nums.sort()

s = []

def dfs():
    if len(s) == M:
        for i in range(M):
            print(s[i], end = " ")
        print()
        return
    
    for i in range(N):
        if nums[i] not in s:
            s.append(nums[i])
            dfs()
            s.pop()

for i in range(N):
    s.append(nums[i])
    dfs()
    s.pop()