# 프로그래머스, 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    
    user_dict = dict()
    for id in id_list:
        user_dict[id] = [0]
    
    # 신고당한 횟수 및, 유저별 신고현황 저장
    for act in report:
        a, b = act.split()
        if b not in user_dict[a]:
            user_dict[b][0] += 1
            user_dict[a].append(b)
    
    # 정지 된 유저 저장
    stop_list = list()
    for key, value in user_dict.items():
        if value[0] >= k:
            stop_list.append(key)
    
    # 메일 전송 횟수 저장
    for _, value in user_dict.items():
        answer.append(len(set(value) & set(stop_list)))
    
    return answer