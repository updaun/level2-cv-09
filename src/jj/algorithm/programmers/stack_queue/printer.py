# source: https://programmers.co.kr/learn/courses/30/lessons/42587

'''
중요도 높은 문서를 먼저 인쇄하는 프린터

- 가장 앞 문서 꺼낸다.
- if: 대기목록에서 중요도가 더 높은 문서 있다면, 앞 문서 대기목록 마지막으로 보낸다.
- else: 앞 문서 인쇄

요청한 문서가 몇 번째로 인쇄되는지 return
'''

def solution(priorities, location):
    # priorities: 중요도가 담긴 배열
    # location: 요청한 문서의 위치
    
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        # 맨 앞 문서 꺼내기
        cur = queue.pop(0)
        
        # 맨 앞 문서보다 중요한 문서가 있다면, 뒤로 넣기
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            # 인쇄한 횟수 count
            answer += 1
            
            # 인쇄한 문서가 요청한 문서라면 return
            if cur[0] == location:
                return answer