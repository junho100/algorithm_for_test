N = int(input())
can = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            can.append(str(i)+str(j)+str(k))
def str_check(a, b):
    cnt = 0
    for i in range(3):
        if a[i] == b[i]:
            cnt += 1
    return cnt

def ball_check(a, b):
    cnt = 0
    for i in range(3):
        if (b[i] in a) and b[i] != a[i]:
            cnt += 1
    return cnt

result = []
op = []
for _ in range(N):
    num, st, ba = map(int, input().split())
    op.append((str(num), st, ba))

for i in range(len(can)):
    for j in range(N):
        num, st, ba = op[j]
        if (str_check(num, can[i]) != st) or (ball_check(can[i], num) != ba):
            break
    else:
        result.append(can[i])
print(len(result))