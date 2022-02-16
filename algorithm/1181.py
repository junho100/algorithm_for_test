words = []
N = int(input())

for _ in range(N):
    d = input()
    if d not in words:
        words.append(d)

words.sort()
words.sort(key = lambda x : len(x))

for i in range(len(words)):
    print(words[i])
