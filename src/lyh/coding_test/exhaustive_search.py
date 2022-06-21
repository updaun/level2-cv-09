# 프로그래머스, 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def evaluate(answers, math_loser):
    score, pos, math_len = 0, 0, len(math_loser)
    while pos < len(answers):
        if answers[pos] == math_loser[pos%math_len]:
            score += 1
        pos += 1
    return score

def solution(answers):
    answer = []
    math_loser_1 = [1, 2, 3, 4, 5]
    math_loser_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_loser_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_loser_list = []
    score_loser_list.append(evaluate(answers, math_loser_1))
    score_loser_list.append(evaluate(answers, math_loser_2))
    score_loser_list.append(evaluate(answers, math_loser_3))
    max_score = max(score_loser_list)
    
    for i, score in enumerate(score_loser_list):
        if score == max_score:
            answer.append(i+1)
    
    return answer