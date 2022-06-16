# source: https://programmers.co.kr/learn/courses/30/lessons/92334

'''
불량 이용자 신고 처리 결과 메일 발송 시스템
- 각 유저는 한 번에 한 명의 유저 신고 가능
- 신고 횟수 제한 x. 서로 다른 유저를 계속해서 신고 가능.
- 한 유저 여러 번 신고 가능하지만, 동일한 유저에 대한 신고 횟수는 1회로 처리

- k번 이상 신고된 유저는 게시판 이용 정지. 
- 해당 유저를 신고한 모든 유저에게 정지 사실 메일로 발송.
- 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지 시키면서 정지 메일 발송
'''

'''
id_list: 이용자의 ID가 담긴 문자열 배열
report: 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
k: 정지 기준이 되는 신고 횟수
'''

# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

from collections import Counter

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    # 중복 제거
    report_no_repeat = list(set(report))
    
    # reporter: 신고자, reported: 신고 받은 유저
    reporter = [x.split(' ')[0] for x in report_no_repeat]
    reported = [x.split(' ')[1] for x in report_no_repeat]
    
    # 신고 받은 횟수에 대한 counter
    counter = Counter(reported)
    
    banned = [x[0] for x in counter.items() if x[1] >= k]
    
    for i in range(len(id_list)):
        user = id_list[i]
        
        for j in range(len(reporter)):
            if user == reporter[j] and reported[j] in banned:
                answer[i] += 1
    
    return answer