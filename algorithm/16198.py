import sys

input = sys.stdin.readline

N = int(input().rstrip())
Ws = list(map(int, input().rstrip().split()))

result = 0
m = 0
def dfs():
    global result, m
    if len(Ws) == 2:
        if result > m:
            m = result
        return
    
    for i in range(1, len(Ws)-1):
        result += (Ws[i-1] * Ws[i+1])
        tmp = Ws.pop(i)
        dfs()
        Ws.insert(i, tmp)
        result -= (Ws[i-1] * Ws[i+1])

for i in range(1, len(Ws) -1):
    result += (Ws[i-1] * Ws[i+1])
    tmp = Ws.pop(i)
    dfs()
    Ws.insert(i, tmp)
    result -= (Ws[i-1] * Ws[i+1])
print(m)
