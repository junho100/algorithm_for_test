import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nums = list(map(int, input().rstrip().split()))
nums.sort()
cans = dict()
s = []

def dfs():
    if len(s) == M:
        tmp = ""
        for i in range(M):
            tmp += str(nums[s[i]])
            tmp += " "
        if tmp not in cans:
            cans[tmp] = True
            t = tmp.split(" ")
            print(" ".join(t))
        return
    for i in range(N):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

for i in range(N):
    s.append(i)
    dfs()
    s.pop()