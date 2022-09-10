# programmers arrow competition task
# https://school.programmers.co.kr/learn/courses/30/lessons/92342

import copy

cases = []
max_score = 0

def calc_score_diff(case, info):
    lion, apech = 0, 0
    for i in range(11):
        if case[10-i] > info[10-i]:
            lion += i
        elif case[10-i] + info[10-i] == 0:
            continue
        else:
            apech += i
    return lion - apech


def dfs(n, info, nth, case):
    global cases, max_score
    
    if nth == 11:
        if n:
            case[10] = n
        score_diff = calc_score_diff(case, info)
        result = copy.deepcopy(case)
        if score_diff <= 0:
            return
        if score_diff > max_score:
            max_score = score_diff
            cases = [result]
        if score_diff == max_score:
            cases.append(result)
        return
    
    if info[nth] < n:
        batt = info[nth] + 1
        case[nth] = batt
        dfs(n-batt, info, nth+1, case)
    case[nth] = 0
    dfs(n, info, nth+1, case)
    return


def solution(n, info):
    q = [0] * 11
    dfs(n, info, 0, q)
    global cases
    
    if cases:
        cases.sort(key = lambda x : x[::-1], reverse=True)
        return cases[0]
    return [-1]