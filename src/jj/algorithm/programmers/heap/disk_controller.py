# source: https://programmers.co.kr/learn/courses/30/lessons/42627

# jobs: 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간]

import heapq
from collections import deque

def solution(jobs):
    # 소요시간, 요청 시점
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    # 제일 빨리 요청된 task를 넣어준다.
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, request_time = heapq.heappop(q)
        
        # 현재 시간이 요청 시점을 지난 후라면 전자, 지나기 전이면 후자.
        current_time = max(current_time + dur, request_time + dur)
        
        # 작업의 요청부터 종료까지 걸린 시간
        total_response_time += current_time - request_time
        
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)