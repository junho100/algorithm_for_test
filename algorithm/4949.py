import sys

input = sys.stdin.readline

while True:
    d = input().rstrip()
    s = []
    if d == ".":
        break

    d = d[:-1]
    check = True
    for word in d:
        if word == "(" or word == "[":
            s.append(word)
        else:
            if word == ")":
                if len(s) == 0 or s[-1] != "(":
                    check = False
                    break
                else:
                    s.pop()
            elif word == "]":
                if len(s) == 0 or s[-1] != "[":
                    check = False
                    break
                else:
                    s.pop()
    if len(s) != 0 or check == False:
        print("no")
    else:
        print("yes")