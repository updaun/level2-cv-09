# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
        
    ban = {}
    
    for singo in set(report):
        singoer, singoee = singo.split()
        
        if singoee in ban:
            ban[singoee].append(singoer)
        else:
            ban[singoee] = [singoer]
        
    for user in ban:
        if len(ban[user]) >= k:
            singoees = ban[user]
            for s in singoees:
                answer[id_list.index(s)] += 1
        
    
    return answer