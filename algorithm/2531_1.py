import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushies = []

for _ in range(N):
    sushies.append(int(input().rstrip()))

sushies += sushies
result = 0
for i in range(N):
    eats = list(set(sushies[i:i+k]))

    if c in eats:
        result = max(result, len(eats))
    else:
        result = max(result, len(eats) + 1)
print(result)
