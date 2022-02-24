import sys

input = sys.stdin.readline

N = int(input().rstrip())

result = 0
candies = []
def dfs(x):
    global result
    if x == N:
        result += 1
        return
    
    for i in range(N):
        check = True

        if len(candies) != 0:
            for candi in candies:
                if candi[0] == x or candi[1] == i or abs(candi[0] - x) == abs(candi[1] - i):
                    check = False
                    break
        if check:
            candies.append((x, i))
            dfs(x+1)
            candies.pop()

dfs(0)
print(result)



