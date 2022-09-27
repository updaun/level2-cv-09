# source: https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    limit, cnt = (len(queue1)-1) * 3 + 1, 0 # 피크에 몰려있을 경우를 고려해서
    
    while (queue1 and queue2) and cnt < limit:
        if q1_sum == q2_sum:  # 두 큐 합이 같으면 종료
            return cnt
        elif q1_sum > q2_sum:  # queue1의 합이 더 크면 queue1에서 빼기
            e = queue1.popleft()
            queue2.append(e)
            q1_sum -= e
            q2_sum += e
        else:  # queue1의 합이 queue2보다 작을 때
            e = queue2.popleft()
            queue1.append(e)
            q1_sum += e
            q2_sum -= e
        cnt += 1
        
    return -1  # 두 큐 합이 같아지지 않으면 -1 반환