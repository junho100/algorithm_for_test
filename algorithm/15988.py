import sys

input = sys.stdin.readline

T = int(input().rstrip())
d = [0]*1000001
d[1] = 1
d[2] = 2
d[3] = 4
last = 3
for _ in range(T):
    n = int(input().rstrip())
    if n <= last:
        print(d[n]%1000000009)
        continue
    else:
        for i in range(last+1, n+1):
            d[i] = d[i-1]%1000000009 + d[i-2]%1000000009 + d[i-3]%1000000009
        last = n
        print(d[n]%1000000009)