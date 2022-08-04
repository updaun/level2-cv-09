# 프로그래머스
# https://programmers.co.kr/app/with_setting/tests/47122/challenges/algorithms/8564

def solution(name_list):
    answer = []
    # 65 ~ 90
    name_unique = set(name_list)
    name_dict = dict()
    
    for name in name_unique:
        name_dict[name] = 65
    
    for name in name_list:
        temp = name + chr(name_dict[name])
        answer.append(temp)
        name_dict[name] += 1

    return answer