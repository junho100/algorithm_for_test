from collections import deque
import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    Ps = list(input().rstrip())
    n = int(input().rstrip())
    cnt = 0
    arr = ""
    if n == 0:
        arr = input().rstrip()
        arr = []
    elif n == 1:
        arr = input().rstrip()
        arr = [int(arr[1:-1])]
    else:
        arr = input().rstrip()
        arr = list(map(int, arr[1:-1].split(",")))
    q = deque(arr)
    check = True

    for P in Ps:
        if P == "R":
            cnt += 11
        elif P == "D":
            if len(q) == 0:
                check = False
                break
            else:
                if cnt% 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if check:
        if cnt % 2 != 0:
            q.reverse()
        print("[", end="")
        if len(q)>= 1:
            for i in range(len(q)-1):
                print(q[i], end=",")
            print(q[len(q)-1], end="")
        print("]")
    else:
        print("error")