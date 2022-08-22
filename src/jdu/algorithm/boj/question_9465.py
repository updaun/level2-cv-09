import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    d = [[0 for i in range(n)] for _ in range(2)]
    s = []
    s.append(list(map(int, input().split())))
    s.append(list(map(int, input().split())))

    d[0][0] = s[0][0]
    d[1][0] = s[1][0]

    for i in range(1, n):
        if i == 1:
            d[0][i] = s[1][0] + s[0][i]
            d[1][i] = s[0][0] + s[1][i]
        else:
            d[0][i] = max(d[1][i-1], d[1][i-2]) + s[0][i]
            d[1][i] = max(d[0][i-1], d[0][i-2]) + s[1][i]

    print(max(d[0][n-1], d[1][n-1]))