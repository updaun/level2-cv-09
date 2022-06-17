# https://programmers.co.kr/learn/courses/30/lessons/92334
 
# 코딩테스트 연습
# 2022 KAKAO BLIND RECRUITMENT
# 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    ban = dict()
    report_dict = dict()
    ban_list = []
    for i in id_list:
        report_dict[i] = []
    
    for i in set(report):
        user_id, report_id = i.split()
        if report_id not in ban.keys():
            ban[report_id] = 1
        else:
            ban[report_id] += 1
        if user_id in report_dict.keys():
            report_dict[user_id].append(report_id)
            
    # 정지된 아이디 정리
    for i in ban.keys():
        if ban[i] >= k:
            ban_list.append(i)
            
    for id in id_list:
        answer.append(len(set(report_dict[id]).intersection(set(ban_list))))
        
    return answer