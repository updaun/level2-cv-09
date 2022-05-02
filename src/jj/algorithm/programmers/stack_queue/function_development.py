# source: https://programmers.co.kr/learn/courses/30/lessons/42586

'''
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포.

progresses: 작업 진도가 적힌 정수 배열
speeds: 작업의 개발 속도가 적힌 정수 배열

각 배포마다 몇 개의 기능이 배포되는지 return
'''

def solution(progresses, speeds):

    answer = []
    time = 0 
    count = 0 # 배포될 기능의 개수
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            # 앞에 있던 작업이 끝난 상태라면,
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer