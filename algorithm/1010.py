import math

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    result = int((math.factorial(b) / (math.factorial(b-a) * math.factorial(a))))

    print(result)
