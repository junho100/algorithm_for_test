from itertools import permutations

def solution(numbers):
    result = []
    answer = 0
    num_list = list(numbers)
    for i in range(1, len(numbers) + 1):
        cans = list(permutations(num_list, i))
        for can in cans:
            num = int("".join(can).strip())
            if num < 2 or num in result:
                continue
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                answer += 1
                result.append(num)
    return answer