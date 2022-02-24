import sys

input = sys.stdin.readline

while True:
    s = []
    d = input().rstrip()
    if d == "0":
        break

    data = d.split()
    K = int(data[0])
    Ks = list(map(int, data[1:]))

    def dfs():
        if len(s) == 6:
            print(" ".join(list(map(str, s))))
            return
        
        for i in range(K):
            if (Ks[i] not in s) and (len(s) == 0 or s[-1] < Ks[i]):
                s.append(Ks[i])
                dfs()
                s.pop()
    dfs()
    print()