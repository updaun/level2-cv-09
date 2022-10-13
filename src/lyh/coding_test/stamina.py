# stamina task
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import *

def try_dungeon(k, dungeons, case):
    num_dungeon = 0
    
    for i in case:
        if k >= dungeons[i][0]:
            num_dungeon += 1
        k -= dungeons[i][1]
        
    return num_dungeon

def solution(k, dungeons):
    answer = -1
    dungeon_len = len(dungeons)
    dungeon_idxs = [i for i in range(dungeon_len)]
    
    for case in permutations(dungeon_idxs, dungeon_len):
        success_dungeon = try_dungeon(k, dungeons, case)
        if dungeon_len == success_dungeon:
            return success_dungeon

        if answer < success_dungeon:
            answer = success_dungeon
    
    return answer