def solution(numbers):
    answer = ""
    num_with_ad = []
    for i in range(len(numbers)):
        tmp = str(numbers[i])*4
        tmp = tmp[:4]
        num_with_ad.append((int(tmp), i))
    
    num_with_ad.sort(reverse = True, key = lambda x : x[0])

    for i in range(len(numbers)):
        answer += str(numbers[num_with_ad[i][1]])
    while len(answer) != 1:
        if answer[0] == "0":
            answer = answer[1:]
        else:
            break
    return answer