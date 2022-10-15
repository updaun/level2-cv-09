# programmers DFS min distance game map task
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 정확도 100점, 효율성 0점


import copy

def DFS(move, x, y, visited, maps, moves):
    if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]):
        return False
    if not maps[x][y]:
        return False
    if x == len(maps) - 1 and y == len(maps[0]) - 1:
        return move
    
    if not visited[x][y] and maps[x][y]:
        visited[x][y] = True
        copy_visited = copy.deepcopy(visited)
        temp = DFS(move + 1, x + 1, y, copy_visited, maps, moves)
        if temp:
            moves.append(temp)
        temp = DFS(move + 1, x - 1, y, copy_visited, maps, moves)
        if temp:
            moves.append(temp)
        temp = DFS(move + 1, x, y + 1, copy_visited, maps, moves)
        if temp:
            moves.append(temp)
        temp = DFS(move + 1, x, y - 1, copy_visited, maps, moves)
        if temp:
            moves.append(temp)

def solution(maps):
    answer = 0
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    moves = list()
    DFS(0, 0, 0, visited, maps, moves)
    if not moves:
        answer = -1
    else:
        answer = min(moves) + 1
    return answer