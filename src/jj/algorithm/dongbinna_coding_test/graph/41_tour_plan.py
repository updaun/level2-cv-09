'''
N개의 여행지. (1~N번으로 여행지 구분)
임의의 두 여행지 사이에 두 여행지를 연결하는 도로 존재할 수 있다. (양방향 이동 가능)
여행 계획이 가능한지의 여부 판단.
'''

'''
입력
첫째 줄: 여행지의 수 N과 여행 계획에 속한 도시의 수 M (1 <= N,M <= 500)
다음 N개의 줄에 걸쳐 N x N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어진다. (1: 연결, 0: 연결 x)
마지막 줄에 여행 계획에 포함된 여행지의 번호들이 주어진다.

출력
가능하다면 YES, 불가능하다면 NO.
'''

'''
Solution
서로소 집합 알고리즘 이용. 그래프에서 노드 간의 연결성을 파악.
여행 계획에 해당하는 모든 노드가 같은 집합에 속한다면 가능한 여행 경로.
'''

# 특정 원소가 속한 집합 찾기
from re import L


def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))

    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")