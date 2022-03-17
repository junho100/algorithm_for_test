import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = []
for _ in range(N):
    coins.append(int(input().rstrip()))

coins.sort(reverse = True)

cnt = 0

for coin in coins:
    if coin > K:
        continue

    cnt += (K // coin)
    K = K%coin

print(cnt)