import copy

def solution(triangle):
    answer = 0
    d = copy.deepcopy(triangle)

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j], d[i-1][j-1]) + triangle[i][j]
    answer = max(d[-1])
    return answer