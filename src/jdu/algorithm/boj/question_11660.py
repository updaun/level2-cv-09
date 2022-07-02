# 시간 초과
'''
import sys
N,M = list(map(int, sys.stdin.readline().split()))
table = []
for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
for i in range(M):
    answer = 0
    x1, y1, x2, y2 = [i-1 for i in list(map(int, sys.stdin.readline().split()))]
    for i in range(x1, x2+1):
        answer += sum(table[i][y1:y2+1])
    print(answer)
'''

import sys
N,M = list(map(int, sys.stdin.readline().split()))
table = []
sum_table = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_table[i][j] = table[i-1][j-1] + sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1]
for i in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    answer = sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]
    print(answer)
