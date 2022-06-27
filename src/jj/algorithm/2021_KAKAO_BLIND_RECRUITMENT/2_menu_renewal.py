# source: https://programmers.co.kr/learn/courses/30/lessons/72411

'''
가장 많이 함께 주문한 단품 메뉴들을 코스요리 메뉴로 구성.
코스요리 최소 2가지 이상의 단품메뉴로 구성.
최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합에만 코스요리 메뉴 후보.
'''

'''
orders: 각 손님들이 주문한 단품메뉴들을 문자열 형식으로 담은 배열
course: 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열
'''

from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        
        combination = []
        
        for order in orders:
        
            combi = list(combinations(order, c))
        
            for i in range(len(combi)):
                combi[i] = sorted(list(combi[i]))
            
            for comb in combi:
                combination.append(''.join(comb))
            
        combination_set = list(set(combination))
        
        combination_dict = dict()
        
        for c in combination_set:
            combination_dict[c] = 0
            
        for c in combination:
            combination_dict[c] += 1
        
        if combination:
            max_order = max(list(combination_dict.values()))
            
            for key, value in combination_dict.items():
                if value == max_order and value > 1:
                    answer.append(key)
    
    return sorted(answer)