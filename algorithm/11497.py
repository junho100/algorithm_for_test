import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    tmp = []
    if N % 2 == 0:
        for i in range(0, N, 2):
            tmp.append(arr[i])
        for i in range(N-1, -1, -2):
            tmp.append(arr[i])
    else:
        for i in range(0, N, 2):
            tmp.append(arr[i])
        for i in range(N-2, -1, -2):
            tmp.append(arr[i])
    result = 0
    for i in range(1, N):
        result = max(result, abs(tmp[i-1] - tmp[i]))
    print(result)