import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    d = list(input().rstrip())
    cnt = 0
    for i in range(len(d)):
        if d[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            break
    
    if cnt < 0 or cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
