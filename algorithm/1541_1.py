import sys

input = sys.stdin.readline

d = input().rstrip()
result = []

a = d.split("-")
for i in a:
    tmp = 0
    plus = i.split("+")
    for p in plus:
        tmp += int(p)
    if len(result) == 0:
        result.append(tmp)
    else:
        result.append(-tmp)
print(sum(result))