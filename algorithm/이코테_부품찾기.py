N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

def b_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

arr.sort()

for target in targets:
    if b_search(arr, target, 0, N-1) == None:
        print("no", end = " ")
    else:
        print("yes", end = " ")