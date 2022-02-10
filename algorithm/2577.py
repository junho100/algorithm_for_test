A = int(input())
B = int(input())
C = int(input())
multi = list(str(A * B * C))
for i in range(10):
    print(multi.count(str(i)))