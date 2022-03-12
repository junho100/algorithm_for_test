import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()
cnt = 0
Pn = ""
for i in range(N):
    Pn += "IO"
else:
    Pn += "I"

for i in range(M-len(Pn)+1):
    if S[i:i+len(Pn)] == Pn:
        cnt += 1
print(cnt)