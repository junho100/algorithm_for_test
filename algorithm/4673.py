def get_d(i):
    result = i
    i_arr = list(map(int, list(str(i))))
    for j in i_arr:
        result += j
    
    return result

ans = [True]*(10001)

for i in range(1, 10001):
    d = get_d(i)
    if d > 10000:
        continue
    else:
        ans[d] = False


for i in range(1, 10001):
    if ans[i]:
        print(i)