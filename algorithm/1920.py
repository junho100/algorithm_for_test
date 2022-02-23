import sys

input = sys.stdin.readline

N = int(input().rstrip())
d = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
targets = list(map(int, input().rstrip().split()))

d.sort()

def b_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

for target in targets:
    if b_search(d, target, 0, N-1) == None:
        print(0)
    else:
        print(1)