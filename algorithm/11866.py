from collections import deque

N, K = map(int, input().split())
cnt = 0
q = deque()
result = []
for i in range(1, N+1):
    q.append(i)

while q:
    now = q.popleft()
    cnt += 1
    if cnt == K:
        result.append(now)
        cnt = 0
        continue
    else:
        q.append(now)

print("<", end = "")
for i in range(len(result)-1):
    print(result[i], end = ", ")
else:
    print(result[len(result)-1], end="")
print(">")