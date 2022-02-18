N = int(input())
a = list(map(int, input().split()))

d = [0]*(101)
d[0] = a[0]
d[1] = max(a[0], a[1])

for i in range(2, N):
    d[i] = max(d[i-2] + a[i], d[i-1])

print(d[N-1])