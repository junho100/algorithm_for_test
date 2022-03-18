import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()

start = 0
end = N-1
now = []
current = (10**10)*2

while start < end:
    left = arr[start]
    right = arr[end]
    tmp = left + right

    if abs(tmp) < abs(current):
        now = [left, right]
        current = tmp
    
    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1

print(*now)