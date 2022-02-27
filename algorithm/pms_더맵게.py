import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    
    while q:
        if q[0] >= K:
            break
        else:
            if len(q) == 1:
                if q[0] < K:
                    answer = -1
                    break
            fir = heapq.heappop(q)
            sec = heapq.heappop(q)
            new = fir + (sec * 2)
            heapq.heappush(q, new)
            answer += 1
    return answer