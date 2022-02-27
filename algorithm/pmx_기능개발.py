from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        if left % speeds[i] != 0:
            q.append(left // speeds[i] + 1)
        else:
            q.append(left // speeds[i])
    cnt = 1
    now = q.popleft()
    while q:
        if q[0] <= now:
            cnt += 1
            q.popleft()
        else:
            answer.append(cnt)
            cnt = 1
            now = q.popleft()
    else:
        if cnt != 0:
            answer.append(cnt)

    return answer
