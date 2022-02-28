T = int(input())
for _ in range(T):
    data = input()
    cnt = 0
    result = 0
    for i in data:
        if i == "O":
            cnt += 1
            result += cnt
        elif i == "X":
            cnt = 0
    print(result)