from itertools import combinations

T = int(input())

for _ in range(T):
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input())
    
    cans = list(combinations(words, 2))

    for can in cans:
        a, b = can
        tmp_a = a + b
        tmp_b = b + a

        if tmp_a == tmp_a[::-1]:
            print(tmp_a)
            break
        elif tmp_b == tmp_b[::-1]:
            print(tmp_b)
            break
    
    else:
        print(0)