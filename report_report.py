def solution(id_list, report, k):
    reported = {}
    return_lst = {i : 0 for i in id_list}

    for i in report:
        a, b = i.split()


        
        reported[b] = reported.get(b,set([])) | {a}
        
        if reported[b] and len(reported[b]) == k:
            for i in reported[b]:
                return_lst[i] += 1
            
    answer = [return_lst[i] for i in return_lst]
    return answer