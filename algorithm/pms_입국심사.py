answer = 0
def solution(n, times):
    start = 1
    end = max(times) * n
    def b_search(start, end, target):
        global answer
        while start <= end:
            mid = (start + end) // 2
            cnt = 0
            for time in times:
                if mid >= time:
                    cnt += mid // time
            
            if cnt < target:
                start = mid + 1
            else:
                answer = mid
                end = mid - 1

    b_search(start, end, n)
    return answer