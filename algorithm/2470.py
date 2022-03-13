import sys

input = sys.stdin.readline

N = int(input().rstrip())
liqs = list(map(int, input().rstrip().split()))

start = 0
end = N-1
cans = []
liqs.sort()
result = (10**10)*2
while start < end:
    left = liqs[start]
    right = liqs[end]

    mixed = left + right

    if abs(result) > abs(mixed):
        result = mixed
        cans = [left, right]
    
    if mixed < 0:
        start += 1
    else:
        end -= 1
print(cans[0], cans[1])