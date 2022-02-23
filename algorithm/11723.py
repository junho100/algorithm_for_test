import sys

input = sys.stdin.readline

S = set([])
All = set([str(i) for i in range(1, 21)])

M = int(input())
for _ in range(M):
    d = input().rstrip().split()
    if d[0] == "add":
        S.add(d[1])
    elif d[0] == "remove":
        S.discard(d[1])
    elif d[0] == "check":
        if d[1] in S:
            print(1)
        else:
            print(0)
    elif d[0] == "toggle":
        if d[1] in S:
            S.discard(d[1])
        else:
            S.add(d[1])
    elif d[0] == "all":
        S = All.copy()
    elif d[0] == "empty":
        S.clear()