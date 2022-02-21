N = int(input())

for i in range(0, N):
        print(" "*i, end ="")
        print("*"*(2*(N)-1 - (2*i)), end = "")
        print(" "*i, end ="")
        print()
