def solution(numbers, target):
    global answer
    answer = 0
    s = []
    def dfs(x):
        global answer
        if x == len(numbers):
            if sum(s) == target:
                answer += 1
            return
        
        for i in range(2):
            if i == 0:
                s.append(numbers[x])
                dfs(x+1)
                s.pop()
            else:
                s.append(numbers[x]*(-1))
                dfs(x+1)
                s.pop()
    dfs(0)
    return answer
