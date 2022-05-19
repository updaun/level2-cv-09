# source: https://programmers.co.kr/learn/courses/30/lessons/43162

def dfs(computers, visited, start):
    stack = [start]
    
    while stack:
        j = stack.pop()
        visited[j] = 1
        
        for i in range(len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    i = 0
    
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        
        i += 1
    
    return answer