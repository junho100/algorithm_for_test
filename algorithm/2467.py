N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1

result = abs(arr[start] + arr[end])
result_arr = [start, end]

while (start < end):
    s = arr[start] + arr[end]

    if abs(s) < result:
        result_arr[0] = start
        result_arr[1] = end
        result = abs(s)
    if s > 0:
        end -= 1
    elif s < 0:
        start += 1
    else:
        result_arr[0] = start
        result_arr[1] = end
        result = abs(s)
        break

print(arr[result_arr[0]], arr[result_arr[1]])