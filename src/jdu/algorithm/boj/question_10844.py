n = int(input())
d = [[0] + [1]*9]
for i in range(1, n):
    temp = []
    for j in range(10):
        if j == 0:
            temp.append(d[i-1][1])
        elif j == 9:
            temp.append(d[i-1][8])
        else:
            temp.append(d[i-1][j-1]+d[i-1][j+1])
    d.append(temp)
print(sum(d[n-1]) % 1000000000)