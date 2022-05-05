# soruce: https://programmers.co.kr/learn/courses/30/lessons/42626

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 힙 큐 알고리즘: https://python.flowdas.com/library/heapq.html

import heapq

def solution(scoville, K):
    answer = 0
    
    h = heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
    
    return answer