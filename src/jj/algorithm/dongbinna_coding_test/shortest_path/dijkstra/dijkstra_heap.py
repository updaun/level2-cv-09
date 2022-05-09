# 시간 복잡도: O(ElogV)
# V: 노드의 개수, E: 간선의 개수

# input()을 더 빠르게 동작하기 위해 sys.std.readline()으로 치환.
import sys
input = sys.stdin.readline

import heapq

INF = int(1e9) # 10억을 무한으로 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# (노드의 개수 + 1)로 할당하여, 노드의 번호를 인덱스로 하여 바로 리스트에 접근할 수 있도록 한다.
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)


# 간선 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정한 뒤, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])