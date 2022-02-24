N, M = map(int, input().split())

array = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j != k:
                tmp = array[i] + array[j] + array[k]
                if tmp <= M:
                    result = max(result, tmp)
print(result)