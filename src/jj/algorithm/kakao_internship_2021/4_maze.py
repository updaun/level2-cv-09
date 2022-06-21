# source: https://programmers.co.kr/learn/courses/30/lessons/81304
# ref: https://www.youtube.com/watch?v=MaVaofAobXw&list=PL6YHvWRMtz7DqcupeeJ1FOTXjZmJPu_XC&index=11

'''
함정으로 이동 시, 이동한 함정과 연결된 모든 화살표의 방향이 바뀐다.
똑같은 함정 방을 두 번째 방문하면 원래 방향의 길로 돌아온다.
탈출하는데 걸리는 최소 시간 구하기.
'''

'''
n: 방의 개수
start: 출발 방의 번호
end: 도착 방의 번호
roads: 
- 통로와 이동시간을 나타내는 2차원 정수 배열
- [P, Q, S]
- P에서 Q로 갈 수 있고, 걸리는 시간 S.

traps: 함정 방의 번호를 담은 정수 배열
'''

import queue

INF = 10e9

def dijkstra(n, graph, src, dst, traps):
    pq = queue.PriorityQueue()
    visited = [[False] * (1<<len(traps)) for _ in range(n+1)]
    
    pq.put((0, src, 0)) # cost, 시작 지점, trap 상태
    
    while not pq.empty():
        cur = pq.get()
        w, u, state = cur
        
        if u == dst:
            return w
        
        if visited[u][state]:
            continue
            
        visited[u][state] = True
        
        curTrapped = False
        trapped = {}
        
        for i in range(len(traps)):
            bit = 1 << i
            
            # i번째 trap이 활성화돼있는 상태라면,
            if state & bit:
                # 현재 도착한 노드 u의 trap이 이미 활성화돼있던 상태라면, 다시 꺼주기
                if traps[i] == u:
                    state &= ~bit
                # 현재 도착한 노드가 아니라면 활성화
                else:
                    trapped[traps[i]] = True
                    
            else:
                # 도착한 곳이 함정 node라면 활성화
                if traps[i] == u:        
                    state |= bit
                    trapped[traps[i]] = True
                    curTrapped = True
                    
        for v in range(1, n+1):
            if v == u:
                continue
            
            nextTrapped = True if v in trapped else False
            
            # trap이 둘 다 꺼져있거나 활성화된 상태라면 graph 정방향으로
            if curTrapped == nextTrapped:
                if graph[u][v] != INF:
                    pq.put((w + graph[u][v], v, state))
            # trap 하나만 켜진거면 역방향
            else:
                if graph[v][u] != INF:
                    pq.put((w + graph[v][u], v, state))
                    
    return INF
                    
def solution(n, start, end, roads, traps):
    
    # 인접 행렬
    graph = [[INF] * (n + 1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for data in roads:
        # 시작 지점, 연결 지점, 비용
        u, v, w = data
        
        if w < graph[u][v]:
            graph[u][v] = w
    
    return dijkstra(n, graph, start, end, traps)