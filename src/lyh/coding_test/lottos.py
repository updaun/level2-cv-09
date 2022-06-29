# 프로그래머스, 로또의 최고순위와 최저순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    score, erase = 0, 0
    
    for num in lottos:
        if num and num in win_nums:
            score += 1
        if not num:
            erase += 1
    # 0 ~ 6
    if erase:
        answer.append(7-score-erase)
        if not score:
            score = 1
        answer.append(7-score)
    else:
        if not score:
            score = 1
        answer.append(7-score)
        answer.append(7-score)

    return answer