N = int(input())
arr = []
each_eles = []
for _ in range(N):
    d = input()
    each_ele = list(set(list(d)))
    each_eles.append(each_ele)
    arr.append(d)
result = 0
for i in range(N):
    for j in range(len(each_eles[i])):
        while (each_eles[i][j] + each_eles[i][j]) in arr[i]:
            arr[i] = arr[i].replace(each_eles[i][j] + each_eles[i][j], each_eles[i][j])
        if arr[i].count(each_eles[i][j]) >= 2:
            break
    else:
        result += 1

print(result)


## 다른풀이

N = int(input())
words = []
for _ in range(N):
    words.append(input())

def solve(word):
    arr = []
    for i in word:
        if i not in arr:
            arr.append(i)
        elif i == arr[-1]:
            continue
        else:
            return 0
    else:
        return 1

result = 0
for i in words:
    result += solve(i)
print(result)