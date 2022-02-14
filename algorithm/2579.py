N = int(input())
stairs = [0]*300
for i in range(N):
    stairs[i] = int(input())

d = [0]*(300)

d[0] = stairs[0]
d[1] = stairs[1] + stairs[0]
d[2] = max(stairs[0], stairs[1]) + stairs[2]
for i in range(3, N):
    d[i] = max(stairs[i-1] + d[i-3], d[i-2]) + stairs[i]

print(d[N-1])