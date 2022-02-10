K = int(input())
result = []
for _ in range(K):
    tmp = int(input())
    if tmp == 0:
        result.pop()
    else:
        result.append(tmp)

print(sum(result))