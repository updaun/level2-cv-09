'''
M개의 우주
각 우주 1부터 N까지 행성

행성의 크기를 알고 있다.
균등한 우주의 쌍이 몇 개인지?
구성이 같은데, 순서만 다른 우주의 쌍은 한 번만 센다.

균등 조건
'''

'''
입력
첫째 줄
우주의 개수 M, 행성 개수 N

둘째 줄
각 우주의 행성의 크기 한 줄에 하나씩
'''

'''
출력
균등한 우주의 쌍 개수
'''

'''
제한
2 <= M <= 10
3 <= N <= 100
1 <= 행성의 크기 <= 10,000
'''

m, n = list(map(int, input().split()))

size = []

for _ in range(m):
    size.append(list(map(int, input().split())))

check = [[] for _ in range(m)]

for i in range(m):
    for j in range(n):
        for k in range(n):
            if size[i][j] < size[i][k]:
                check[i].append(0)
            elif size[i][j] == size[i][k]:
                check[i].append(1)
            else:
                check[i].append(2)

cnt = 0

for i in range(m):
    for j in range(i+1, m):

        if check[i] == check[j]:
            cnt += 1

print(cnt)
