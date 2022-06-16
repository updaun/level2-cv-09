# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    
    total = len(answers)
    one = []
    two = []
    to = [1,3,4,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    for i in range(total):
        one.append(i%5+1)
        if i%2 == 0:
            two.append(2)
        else:
            mod = int(((i+1)/2)%4)
            two.append(to[mod-1])
    if total <= len(three):
        three = three[:total]
    else:
        while len(three) < total:
            three = three + three
            three = three[:total]
    
    score = [0,0,0]
    for i, a in enumerate(zip(one, two, three)):
        o, t, h = a
        if answers[i] == o:
            score[0] += 1
        if answers[i] == t:
            score[1] += 1
        if answers[i] == h:
            score[2] += 1
    top = max(score)
    for i, s in enumerate(score):
        if s == top:
            answer.append(i+1)
    return sorted(answer)