# DynamicProgramming task
# Solve by in-place arithmetic
# Solve by adding the larger of the previous values.

def solution(triangle):
    answer = 0
    for i, line in enumerate(triangle):
        if i == 0: continue
        for j, node in enumerate(line):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(line) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer = max(triangle[-1])
    return answer