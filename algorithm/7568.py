N = int(input())
data = []
rank = [0]*(N)
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    
    rank[i] = cnt + 1

for i in range(N-1):
    print(rank[i], end=" ")
print(rank[N-1])