import sys

input = sys.stdin.readline

N ,M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
result = 0

left, right = 0, 1

while right <= N and left <= right:
    s_arr = arr[left:right]
    tmp = sum(s_arr)

    if tmp == M:
        result += 1
        right += 1
    elif tmp < M:
        right += 1
    elif tmp > M:
        left += 1

print(result)