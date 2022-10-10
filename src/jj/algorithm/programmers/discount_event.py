# source: https://school.programmers.co.kr/learn/courses/30/lessons/131127

'''
일정한 금액 지불하면 10일 동안 회원 자격.
회원 대상 매일 한 가지 제품 할인 행사.
할인 제품 하루에 하나씩만 구매 가능.
원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입.

회원등록시 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return
'''

def solution(want, number, discount):
    
    answer = 0
    
    want_dict = dict()
    
    for w, n in zip(want, number):
        want_dict[w] = n
    
    for i in range(len(discount)-9):
        want_dict_copy = want_dict.copy()
        
        for j in range(10):
            if discount[i+j] in want:
                want_dict_copy[discount[i+j]] -= 1
        
        if max(want_dict_copy.values()) < 1: 
            answer += 1
        
    return answer