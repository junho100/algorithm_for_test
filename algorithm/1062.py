import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = []
must = ["a", "n", "t", "i", "c"]

for _ in range(N):
    words.append(list(set(input().rstrip())))

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

learn = [False]*(26)
result = 0
for i in must:
    learn[ord(i) - ord("a")] = 1

def dfs(idx, cnt):
    global result
    if cnt == K - 5:
        read_cnt = 0

        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord("a")]:
                    check = False
            
            if check:
                read_cnt += 1
        
        result = max(read_cnt, result)
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

dfs(0, 0)
print(result)