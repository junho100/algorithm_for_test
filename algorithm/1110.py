N = int(input())

def rule(num):
    num_str = ""
    if num < 10:
        num_str = "0"+str(num)
    else:
        num_str = str(num)
    s = sum(list(map(int, list(num_str))))
    s_str = ""
    if s < 10:
        s_str = "0" + str(s)
    else:
        s_str = str(s)
    return int(num_str[1] + s_str[1])

target = rule(N)
result = 1
while target != N:
    target = rule(target)
    result += 1

print(result)
