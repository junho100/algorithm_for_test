import sys

sys = sys.stdin.readline

N, M = map(int, input().rstrip().split())

s = []

def dfs():
    if len(s) == M:
        print(" ".join(list(map(str, s))))
        return
    
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()