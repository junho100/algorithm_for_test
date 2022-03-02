import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushis = []

for _ in range(N):
    sushis.append(int(input().rstrip()))
left, right = 0, 0
result = 0

while left != N:
    right = left + k
    case = set()
    check = True
    for i in range(left,right):
        i = i % N

        case.add(sushis[i])
        if sushis[i] == c:
            check = False
    
    cnt = len(case)
    if check:
        cnt += 1
    result = max(result, cnt)
    left += 1

print(result)