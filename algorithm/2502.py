import sys

input = sys.stdin.readline

D, K = map(int, input().rstrip().split())
d = [[0, 0] for _ in range(31)]

d[1][0] = 1
d[2][1] = 1

for i in range(3, D+1):
    for j in range(2):
        d[i][j] = d[i-1][j] + d[i-2][j]

result = [0, 0]

for i in range(1, 100001):
    a = d[D][0]*i
    if ((K-a)%d[D][1] == 0) and (i <= (K-a)//d[D][1]):
        result[0] = i
        result[1] = (K-a)//d[D][1]
        break
print(result[0])
print(result[1])