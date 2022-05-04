# soruce: https://programmers.co.kr/learn/courses/30/lessons/81303

# 정확성 테스트는 통과하나, 효율성 테스트에서 모두 실패.

'''
n: 표의 행 개수
k: 처음 선택된 행의 위치
cmd: 명령어가 담긴 문자열 배열

명령어
"U X": 현재 선택된 행에서 X칸 위에 있는 행 선택.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행 선택.
"C": 현재 선택된 행 삭제 후, 아래 행 선택. 삭제된 행이 마지막 행인 경우 바로 윗 행 선택.
"Z": 최근에 삭제된 행을 원래 그 자리로 복구. 선택된 행 바뀌지 않는다.
'''

# 모든 명령어 수행 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시.

from collections import deque
import numpy as np

def solution(n, k, cmd):
    
    answer = ''
    
    table = [[i, i] for i in range(n)] # [인덱스, 값]
    
    removed_queue = deque()
    
    for c in cmd:
        c = c.split(' ')
        
        if c[0] == 'U':
            k = k - int(c[1])
        elif c[0] == 'D':
            k = k + int(c[1])
        elif c[0] == "C":
            removed_queue.append(table[k])
            del table[k]
            
            if k == len(table):
                k -= 1
            else:    
                for i in range(k, len(table)):
                    table[i][0] -= 1     
            
        else:
            restored = removed_queue.pop()
            table.insert(restored[0], [restored[0], restored[1]])
            
            for i in range(restored[0]+1, len(table)):
                table[i][0] += 1
            
            if restored[0] <= k:
                k += 1
    
    removed = []
    
    for q in removed_queue:
        removed.append(q[1])
    
    for i in range(n):
        if i in sorted(removed):
            answer += 'X'
        else:
            answer += 'O'
    
    return answer