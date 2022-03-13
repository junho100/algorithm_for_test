import sys

input = sys.stdin.readline

N = int(input().rstrip())
vips = []
M = int(input().rstrip())

for _ in range(M):
    vips.append(int(input().rstrip()))

d = [1, 1, 2]

for i in range(3, 41):
    d.append(d[i-1] + d[i-2])


result = 1
tmp = 0
for i in range(1, N+1):
    if i not in vips:
        tmp += 1
    else:
        if tmp >= 1:
            result *= d[tmp]
            tmp = 0
else:
    if tmp >= 1:
        result *= d[tmp]
        tmp = 0
print(result)