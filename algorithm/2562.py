arr = []
for _ in range(9):
    arr.append(int(input()))

m = max(arr)
print(m)
print(arr.index(m)+1)