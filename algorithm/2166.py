N = int(input())
left = 0
right = 0
cors = []
for _ in range(N):
    x, y = map(int, input().split())
    cors.append([x, y])
x, y = cors[0]
cors.append([x, y])

for i in range(N):
    left += (cors[i][0] * cors[i+1][1])
    right += (cors[i][1] * cors[i+1][0])
result = round(abs(left - right)/2, 1)
print(result)