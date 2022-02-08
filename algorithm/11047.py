N, K = map(int, input().split())

coins = []
for _ in range(N):
    tmp = int(input())
    if tmp > K:
        continue
    else:
        coins.append(tmp)

result = 0
coins = coins[::-1]
for i in range(len(coins)):
    result += K // coins[i]
    K = K % coins[i]

print(result)
