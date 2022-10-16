# source: https://school.programmers.co.kr/learn/courses/30/lessons/131129

'''
1. 최소한의 다트로 0점 만들기
2. 싱글/불을 최대한 많이 던지기

1~20. 싱글, 더블, 트리플, 불
'''

def solution(target):
    
    # 얻을 수 있는 점수 score에 저장
    score = [50]
    
    for i in range(1, 21):
        score.extend([i, i*2, i*3])
    
    score = list(set(score))
    
    memo = [[target, 0] for _ in range(target+1)]
    
    # 한 번 던져서 얻을 수 있는 경우 memo에 추가.
    for s in score:
        if s <= target:
            memo[s][0] = 1
            
            if s <= 20 or s == 50:
                memo[s][1] = 1

    for i in range(1, len(memo)):
        for s in score:
            if i + s <= target:
                # 더 적게 던져서 target 점수를 얻을 수 있는 경우
                if memo[i + s][0] > memo[i][0] + memo[s][0]:
                    memo[i + s][0] = memo[i][0] + memo[s][0]
                    memo[i + s][1] = memo[i][1] + memo[s][1]
                
                # 같은 횟수의 다트를 던진 경우, 싱글/불을 더 많이 던진 경우로 저장.
                elif memo[i + s][0] == memo[i][0] + memo[s][0]:
                    memo[i + s][1] = max(memo[i + s][1], memo[i][1] + memo[s][1])
    
    return memo[-1]