from itertools import combinations

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

result = int(1e9)

def getSum(team1):
    team2 = [i for i in [j for j in range(N)] if i not in team1]
    S1 = 0
    S2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            if i == j:
                continue
            S1 += S[team1[i]][team1[j]]
            S2 += S[team2[i]][team2[j]]
    
    return S1, S2

can = list(combinations([i for i in range(N)], N//2))
for i in can:
    team1 = i
    S1, S2 = getSum(team1)

    if result > abs(S1 - S2):
        result = abs(S1 - S2)

print(result)
    