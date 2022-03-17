import sys

input = sys.stdin.readline

N = int(input().rstrip())
times = list(map(int, input().rstrip().split()))

tmp = 0
d = [0]*(N)
times.sort()

for i in range(len(times)):
    tmp += times[i]
    d[i] = tmp
print(sum(d))