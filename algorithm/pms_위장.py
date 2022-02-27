def solution(clothes):
    col = dict()
    for cloth in clothes:
        name, kind = cloth
        if kind in col:
            col[kind].append(name)
        else:
            col[kind] = [name]
    
    keys = list(col.keys())
    answer = 1
    for key in keys:
        tmp = len(col[key]) + 1
        answer *= tmp
    answer -= 1
    return answer