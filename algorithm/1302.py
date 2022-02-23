import sys

input = sys.stdin.readline

N = int(input().rstrip())
dic = dict()
for _ in range(N):
    key = input().rstrip()
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] += 1
keys = sorted(list(dic.keys()), reverse=True)
result = ""
num = 0
for key in keys:
    if dic[key] >= num:
        result = key
        num = dic[key]

print(result)
