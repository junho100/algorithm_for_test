N = int(input())
INF = 5001
dp = [INF]*(5001)

dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if dp[N] >= INF:
    print(-1)
else:
    print(dp[N])