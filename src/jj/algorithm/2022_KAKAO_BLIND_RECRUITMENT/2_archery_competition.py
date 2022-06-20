# source: https://programmers.co.kr/learn/courses/30/lessons/92342
# ref: https://www.youtube.com/watch?v=dzncNbPMiB4&list=PL6YHvWRMtz7CSFajyWLBwdCql25khPES-&index=4

def solution(n, info):
    answer = [0] * 11
    tmp = [0] * 11 # 라이언이 쏜 화살 임시 저장
    maxDiff = 0
    
    
    '''
    라이언이 쏠 수 있는 모든 경우의 수
    '''
    # 1을 왼쪽으로 10번 shift. (1024)
    # 1~1023까지의 subset
    # for subset in range(1, 1024):
    for subset in range(1, 1 << 10):
        ryan = 0
        apeach = 0
        cnt = 0 # 라이언이 쏜 화살의 갯수
        
        # 0점을 제외한 1부터 10점까지만
        for i in range(10):
            # subset과 일치하는 것이 있다면, i번째 과녁에서 라이언이 이기게 만든다.
            if subset & (1 << i):
                ryan += 10 - i
                # 어피치가 쏜 것보다 1발 더 쏘게.
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                
                # 어피치가 한 개라도 쐈다면, 어피치 점수
                if info[i]:
                    apeach += 10 - i 
        
        # 화살의 갯수를 더 써야하는 경우 버리기
        if cnt > n: continue
        
        # 남은 화살 0점으로
        tmp[10] = n - cnt
        
        if ryan - apeach == maxDiff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
                    
        elif ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = tmp[:] # copy
    
    if maxDiff == 0:
        return [-1]
    
    return answer