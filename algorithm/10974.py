from itertools import permutations
import sys

input = sys.stdin.readline
N = int(input().rstrip())
arr = [i for i in range(1, N+1)]

cans = list(permutations(arr, N))

cans.sort()

for can in cans:
    for i in can:
        print(i, end = " ")
    print()