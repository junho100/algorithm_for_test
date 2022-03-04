import sys

input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
INF = int(1e9)
cnt = 0
tmp = A

result = INF

def dfs(x):
    global tmp, cnt, result
    if x == B:
        result = min(result, cnt)
        return
    
    if x * 2 <= B:
        tmp *= 2
        cnt += 1
        dfs(tmp)
        cnt -= 1
        tmp = tmp// 2
    if int(str(x) + "1") <= B:
        tmp = int(str(tmp) + "1")
        cnt += 1
        dfs(tmp)
        cnt -= 1
        tmp = int(str(tmp)[:-1])
        
dfs(A)
if result >= INF:
    print(-1)
else:
    print(result + 1)