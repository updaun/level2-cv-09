# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    score = '0123456789'
    bonus = 'SDT'
    ans = {1:0, 2:0, 3:0}
    chance = 1
    for s in dartResult:
        if s in score:
            if ans[chance] > 0:
                ans[chance] = ans[chance]*10 + int(s)
            else:
                ans[chance] = int(s)
        elif s in bonus:
            ans[chance] = ans[chance]**(bonus.index(s)+1)
            chance += 1
        elif s == "*":
            if chance == 2:
                ans[chance-1] *= 2
            else:
                ans[chance-2] *= 2
                ans[chance-1] *= 2
        else:
            ans[chance-1] *= -1    
    return sum(ans.values())