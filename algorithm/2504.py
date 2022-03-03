import sys

input = sys.stdin.readline

words = list(input().rstrip())
q = []

for word in words:
    if word == "(" or word == "[":
        q.append(word)
    elif word == ")":
        if (len(q) != 0) and (q[-1] == "("):
            q.pop()
        else:
            print(0)
            exit()

    elif word == "]":
        if (len(q) != 0) and (q[-1]== "["):
            q.pop()
        else:
            print(0)
            exit()


def solve(strings):
    tmp = []
    nums = []
    for string in strings:
        if string == "(" or string == "[":
            q.append(string)
            tmp.append(string)
            continue
        if string == ")":
            q.pop()
            tmp.append(string)
        elif string == "]":
            q.pop()
            tmp.append(string)
        if len(q) == 0:
            if len(tmp) == 2 and tmp[0] == "(":
                nums.append(2)
            elif len(tmp) == 2 and tmp[0] == "[":
                nums.append(3)
            else:
                if tmp[0] == "(":
                    nums.append(2 * solve(tmp[1:-1]))
                elif tmp[0] == "[":
                    nums.append(3 * solve(tmp[1:-1]))
            tmp = []
    return sum(nums)

result = solve(words)
print(result)