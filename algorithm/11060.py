import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

d = [int(1e9)]*1001
d[0] = 0
for i in range(N):
    for j in range(i+1, i+1+A[i]):
        if j > 1000:
            break

        d[j] = min(d[j], d[i]+1)
if d[N-1] >= int(1e9):
    print(-1)
else:
    print(d[N-1])