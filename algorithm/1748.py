import sys

input = sys.stdin.readline

N = int(input().rstrip())
l = len(str(N))
result = 0
for i in range(0, l):
    if i == (l-1):
        for j in range(10**i, N+1):
            result += (i+1)
    else:
        for j in range(10**i, 10**(i+1)):
            result += (i+1)
print(result)