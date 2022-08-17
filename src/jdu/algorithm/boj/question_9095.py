d = [0] * 13
d[1], d[2], d[3] = 1, 2, 4
n = int(input())
for _ in range(n):
    t = int(input())
    for i in range(4, t+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]
    print(d[t])