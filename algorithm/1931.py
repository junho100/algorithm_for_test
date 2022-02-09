import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x : (x[1], x[0]))

result = 0
now = 0
for i in range(len(arr)):
    if arr[i][0] >= now:
        result += 1
        now = arr[i][1]

print(result)