import sys

input = sys.stdin.readline

S = int(input().rstrip())
tmp = S * 2
if S == 1:
    print(1)
for i in range(1, S+1):
    if i*(i+1) > tmp:
        print(i-1)
        break