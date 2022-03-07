import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
nums.insert(0, 0)
M = int(input().rstrip())
INF = int(1e9)
d = [[False]*(N+1) for _ in range(N+1)]
for i in range(0, N+1):
    d[i][i] = True
for l in range(2, N+1):
    for start in range(1, N-l+2):
        end = start + l - 1

        if nums[start] == nums[end]:
            if (end - start) == 1:
                d[start][end] = True
            elif d[start+1][end-1] == True:
                d[start][end] = True
                

for _ in range(M):
    s, e = map(int, input().rstrip().split())

    if d[s][e]:
        print(1)
    else:
        print(0)