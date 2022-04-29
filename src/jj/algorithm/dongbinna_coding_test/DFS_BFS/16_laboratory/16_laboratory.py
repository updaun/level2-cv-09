n, m = map(int, input().split())

# 초기 맵 리스트
init_map = []

for _ in range(n):
    init_map.append(list(map(int, input().split())))

# 벽을 세운 후 맵 리스트
map_list = [[0] * m for _ in range(n)]

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기 (x, y) : 바이러스의 좌표
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            # 빈 공간이라면 해당 위치에 바이러스 배치 후 재귀적으로 수행
            if map_list[nx][ny] == 0:
                map_list[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역 크기를 계산하는 메서드
def get_score():
    score = 0

    for i in range(n):
        for j in range(m):
            if map_list[i][j] == 0:
                score += 1

    return score

# DFS를 이용해 벽을 설치하하며, 매번 안전 영역 크기 계산
def dfs(count):
    global result

    # 울타리 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                map_list[i][j] = init_map[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if map_list[i][j] == 2:
                    virus(i, j)
        
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())

        return 
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if init_map[i][j] == 0:
                init_map[i][j] = 1
                count += 1

                dfs(count)

                init_map[i][j] = 0
                count -= 1

dfs(0)
print(result)