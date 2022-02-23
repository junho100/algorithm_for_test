import sys

input = sys.stdin.readline

S = input().rstrip()
result = []
tmp = []
no = False
for word in S:
    tmp.append(word)
    if word == ">":
        result.append("".join(tmp))
        tmp = []
        no = False
    if word == " ":
        if no == False:
            tmp = tmp[::-1][1:]
            result.append("".join(tmp) + " ")
            tmp = []
    elif word == "<":
        tmp = tmp[::-1][1:]
        result.append("".join(tmp))
        tmp = ["<"]
        no = True
else:
    if len(tmp) != 0:
        result.append("".join(tmp[::-1]))
print("".join(result))