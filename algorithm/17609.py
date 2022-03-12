import sys

input = sys.stdin.readline
N = int(input().rstrip())

def isSPal(k, left, right):
    while left < right:
        if k[left] != k[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

def isPal(k):
    start = 0
    end = len(k)-1
    check = True
    while start < end:
        if k[start] != k[end]:
            left_c = isSPal(k, start+1, end)
            right_c = isSPal(k, start, end-1)

            if left_c or right_c:
                return 1
            else:
                return 2
        else:
            start += 1
            end -= 1
    
    if check:
        return 0
    else:
        return 2

for _ in range(N):
    a = input().rstrip()
    print(isPal(a))