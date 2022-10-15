# source: https://school.programmers.co.kr/learn/courses/30/lessons/131705

'''
학생들 각자 번호.
학교 학생 3명의 정수 번호를 더했을 때 0이 되면 '삼총사'

삼총사를 만들 수 잇는 방법의 수 return
'''

def solution(number):
    answer = 0
    
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i != j and i != k and j != k and not sum([number[i], number[j], number[k]]):
                    answer += 1
    
    return answer / 6