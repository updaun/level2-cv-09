# 프로그래머스, 사라지는 발판

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def inRange(board, loc):
    N, M = len(board), len(board[0])
    return 0 <= loc[0] and loc[0] < N and 0 <= loc[1] and loc[1] < M


def isFinished(board, loc):    
    for i in range(4):
        ny, nx = loc[0] + dy[i], loc[1] + dx[i]
        if inRange(board, [ny, nx]) and board[ny][nx]:
            return False
    return True


def dfs(board, aloc, bloc):
    if isFinished(board, aloc):
        return [False, 0]
    if aloc == bloc:
        return [True, 1]
    
    can_win = False
    min_turn, max_turn = 9999999, 0
    
    for i in range(4):
        ny, nx = aloc[0] + dy[i], aloc[1] + dx[i]
        if not inRange(board, [ny, nx]) or not board[ny][nx]:
            continue
        
        board[aloc[0]][aloc[1]] = 0
        res = dfs(board, bloc, [ny, nx])
        board[aloc[0]][aloc[1]] = 1
        
        if not res[0]:
            can_win = True
            min_turn = min(min_turn, res[1])
        elif not can_win:
            max_turn = max(max_turn, res[1])

    turn = min_turn if can_win else max_turn
    return [can_win, 1 + turn]
              

def solution(board, aloc, bloc):
    return dfs(board, aloc, bloc)[1]