import sys

input = sys.stdin.readline

N = input().rstrip()
t = input().rstrip()

idx = 0
cnt = 0
while True:
    end = idx + len(t)

    if end > len(N):
        break

    if N[idx:end] == t:
        cnt += 1
        idx += len(t)
    else:
        idx += 1
print(cnt)