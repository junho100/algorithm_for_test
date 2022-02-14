N = int(input())

a = [0]*(91)
b = [0]*(91)

a[1] = 0
a[2] = 1
b[1] = 1
b[2] = 0

for i in range(3, N+1):
    a[i] = b[i-1] + a[i-1]
    b[i] = a[i-1]

if (N == 1):
    print(1)
elif (N == 2):
    print(1)
else:
    print(2*a[N-1] + b[N-1])