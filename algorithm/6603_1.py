import sys

input = sys.stdin.readline

while True:
    d = input().rstrip().split()

    if d[0] == "0":
        break

    k = int(d[0])
    nums = list(map(int, d[1:]))

    s = []

    def dfs():
        if len(s) == 6:
            print(*s)
            return
        
        for i in range(k):
            if nums[i] not in s and s[-1] < nums[i]:
                s.append(nums[i])
                dfs()
                s.pop()
    
    for i in range(k):
        s.append(nums[i])
        dfs()
        s.pop()
    print()