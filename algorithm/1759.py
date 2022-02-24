import sys

input = sys.stdin.readline

L, C = map(int, input().rstrip().split())
words = list(input().rstrip().split())
words.sort()
m = ["a", "e", "i", "o", "u"]

s = []

def dfs():
    if len(s) == L:
        cnt = [0, 0] # m, not m
        for i in range(L):
            if s[i] in m:
                cnt[0] += 1
            else:
                cnt[1] += 1
        
        if cnt[0] >= 1 and cnt[1] >= 2:
            print("".join(s))
        return
    
    for i in range(C):
        if words[i] not in s and (len(s) == 0 or ord(s[-1]) < ord(words[i])):
            s.append(words[i])
            dfs()
            s.pop()

dfs()