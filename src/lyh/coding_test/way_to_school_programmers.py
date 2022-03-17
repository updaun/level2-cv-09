# DynamicProgramming task
# Solve by in-place arithmetic
# Solve by adding the left value and upper value

def solution(m, n, puddles):
    answer = 0
    path = [[1]*m for _ in range(n)]
    
    for puddle in puddles:
        path[puddle[1]-1][puddle[0]-1] = 0
        
    for i, line in enumerate(path):
        for j, node in enumerate(line):
            if node == 0 or i+j == 0:
                continue
            if i == 0:
                path[i][j] = path[i][j-1]
            elif j == 0:
                path[i][j] = path[i-1][j]
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]

    answer = path[-1][-1] % 1000000007    
    return answer