# https://school.programmers.co.kr/learn/courses/30/lessons/131704

'''
컨테이너 벨트 한 방향으로 진행 가능해서 벨트에 놓인 순서대로 (1번 상자부터) 내릴 수 있다.
컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면, 실을 순서가 될 때까지 잠시 다른 곳(보조 컨테이너 벨트)에 보관.

보조 컨테이너 맨 앞의 상자만 뺄 수 있다.
'''

def solution(order):
    
    answer = 0
    
    b1 = [i for i in range(len(order), 0, -1)]
    b2 = []
    
    order.reverse()
    
    while order:
        if b1 and b1[-1] == order[-1]:
            answer += 1
            b1.pop()
            order.pop()
        elif b2 and b2[-1] == order[-1]:
            answer += 1
            b2.pop()
            order.pop()
        elif b1:
            b2.append(b1.pop())
        else:
            break
    
    return answer