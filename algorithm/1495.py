import sys

input = sys.stdin.readline

N ,S ,M = map(int, input().rstrip().split())
vols = list(map(int, input().rstrip().split()))

d_1 = [False for _ in range(M+1)]
d_2 = [False for _ in range(M+1)]
d_1[S] = True
for vol in vols:
    for i in range(M+1):
        if d_1[i]:
            if i + vol <= M:
                d_2[i + vol] = True
            if i - vol >= 0:
                d_2[i - vol] = True
    
    d_1 = d_2
    d_2 = [False for _ in range(M+1)]
result = -1
for i in range(M, -1 ,-1):
    if d_1[i]:
        result = i
        break
print(result)