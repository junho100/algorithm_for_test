import sys

input = sys.stdin.readline

L, C = map(int, input().rstrip().split())
words = input().rstrip().split()
words.sort()
al = ["a", "e", "i", "o", "u"]
s = []

def dfs():
    if len(s) == L:
        m_cnt = 0
        j_cnt = 0

        for i in range(5):
            m_cnt += s.count(al[i])
        j_cnt = len(s) - m_cnt

        if m_cnt >= 1 and j_cnt >= 2:
            print("".join(s))
        return
    
    for i in range(C):
        if words[i] not in s and ord(s[-1]) < ord(words[i]):
            s.append(words[i])
            dfs()
            s.pop()

for i in range(C):
    s.append(words[i])
    dfs()
    s.pop()

