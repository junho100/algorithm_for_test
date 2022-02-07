def solution(id_list, report, k):
    answer = [0]*(len(id_list))
    report_cnt = [0]*(len(id_list))
    report_ppl = [[] for _ in range(len(id_list))]
    report = list(set(report))
    for i in range(len(report)):
        a, b = report[i].split(" ")
        a_idx = id_list.index(a)
        b_idx = id_list.index(b)
        report_ppl[a_idx].append(b)
        report_cnt[b_idx] += 1
    for i in range(len(id_list)):
        if report_cnt[i] >= k:
            for j in range(len(id_list)):
                if id_list[i] in report_ppl[j]:
                    answer[j] += 1
    

    return answer