# programmers divide power grid
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

graph = dict()
from collections import deque

def BFS(start):
    visited = list()
    queue = deque([start])
    count = 0
    
    while queue:
        n = queue.popleft()
        count += 1
        if n not in visited:
            visited.append(n)
            queue += [node for node in graph[n] if node not in visited]
    return count

def solution(n, wires):
    answer = -1
    
    for v1, v2 in wires:
        if v1 not in graph:
            graph[v1] = [v2]
        else:
            graph[v1].append(v2)
        if v2 not in graph:
            graph[v2] = [v1]
        else:
            graph[v2].append(v1)
    
    answer_list = list()
    # wires하나씩 끊기어서 개수 차이 새보기
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        v1_cnt = BFS(v1)
        v2_cnt = BFS(v2)
        graph[v1].append(v2)
        graph[v2].append(v1)
        answer_list.append(abs(v1_cnt - v2_cnt))

    return min(answer_list)