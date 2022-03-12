N = int(input())
m = 10**(N+2)
M = 0
arr = input().split()
visited = [False]*10
s = []

def check(idx, prev, now):
    if arr[idx] == ">":
        if prev > now:
            return True
    else:
        if prev < now:
            return True
    return False

def dfs():
    global m, M
    if len(s) == (N+1):
        tmp = int("".join(s))
        m = min(m, tmp)
        M = max(M, tmp)
        return
    
    for i in range(10):
        if (not visited[i]) and check(len(s)-1, int(s[-1]), i):
            s.append(str(i))
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False

for i in range(10):
    s.append(str(i))
    visited[i] = True
    dfs()
    s.pop()
    visited[i] = False
M = str(M)
m = str(m)
if len(M) != (N+1):
    M = "0"*(N+1-len(M)) + str(M)
if len(m) != (N+1):
    m = "0"*(N+1-len(m)) + str(m)
print(M)
print(m)