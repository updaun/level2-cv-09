# source: https://school.programmers.co.kr/learn/courses/30/lessons/134239#

'''
기능 목록
- 우박수열 구현
- 각 구간 마다의 면적 계산
- 주어진 ranges의 정적분 결과 result에 append (주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의)
'''

def getHailSequence(k):
    
    hail_sequence = [k]
    
    while k != 1:
        if k % 2:
            k = k * 3 + 1
        else:
            k /= 2
        
        hail_sequence.append(k)
    
    return hail_sequence

def getArea(hail_sequence):
    area_list = []
    
    for i in range(len(hail_sequence) - 1):
        a = hail_sequence[i]
        b = hail_sequence[i + 1]
        
        area = (a + b) / 2
        area_list.append(area)
    
    return area_list

def solution(k, ranges):
    answer = []
    
    hail_sequence = getHailSequence(k)
    area_list = getArea(hail_sequence)
    
    for range in ranges:
        a = range[0]
        b = len(area_list) + range[1]
        
        if a == b:
            answer.append(0.0)
        elif a > b:
            answer.append(-1.0)
        else:
            answer.append(sum(area_list[a:b]))
    
    return answer