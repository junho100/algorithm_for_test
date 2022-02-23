import sys

input = sys.stdin.readline

S = list(input().rstrip())
result = []
for i in range(len(S)):
    result.append(S[i:])

result.sort()

for i in range(len(result)):
    print("".join(result[i]))