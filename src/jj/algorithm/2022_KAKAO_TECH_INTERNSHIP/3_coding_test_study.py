'''
source: https://school.programmers.co.kr/learn/courses/30/lessons/118668

ref
- https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
- https://school.programmers.co.kr/questions/35405
- https://school.programmers.co.kr/questions/35386
'''

'''
문제를 풀기 위해서 '알고력' & '코딩력'

'알고력' 높이기 위해 알고리즘 공부. 1을 높이기 위해 1의 시간.
'코딩력' 높이기 위해 코딩 공부. 1을 높이기 위해 1의 시간.

현재 풀 수 있는 문제 중 하나를 풀어 '알고력'과 '코딩력'을 높인다.
같은 문제 여러 번 푸는 것 가능.

주어진 모든 문제를 풀 수 잇는 '알고력'과 '코딩력'을 얻는 최단시간 구하기.
'''

'''
alp: 알고력 (0 <= alp <= 150)
cop: 코딩력 (0 <= cop <= 150)
problems: 문제의 정보를 담은 2차원 정수 배열 [alp_req, cop_req, alp_rwd, cop_rwd, cost]
'''

def solution(alp, cop, problems):
    
    max_alp, max_cop = alp, cop # 현재 알고력과 코딩력이 이미 problems의 required 보다 클 경우 고려.
    
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
    
    # dp[alg][cop]: 해당 알고력과 코딩력에 도달하기 위해 걸리는 최단 시간
    dp = [[150] * (max_cop+1) for _ in range(max_alp+1)]
    
    dp[alp][cop] = 0 # 현재 알고력과 코딩력에서 걸리는 시간 0으로 초기화.
    
    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            if a < max_alp: dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            if c < max_cop: dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    # 얻은 알고력과 코딩력이 문제 required 보다 크다면 문제 required 요구치에 저장.
                    alp_rwd, cop_rwd = min(max_alp, alp_rwd + a), min(max_cop, cop_rwd + c)
                    
                    dp[alp_rwd][cop_rwd] = min(dp[alp_rwd][cop_rwd], dp[a][c] + cost)
    
    return dp[max_alp][max_cop]