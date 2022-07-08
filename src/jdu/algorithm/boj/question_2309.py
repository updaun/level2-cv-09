import sys
drawf = []
for i in range(9):
    drawf.append(int(sys.stdin.readline()))
target = sorted(drawf)
temp = 0
while sum(target[temp:]) < 100:
    temp += 1
else:
    for i in target[temp:temp+8]:
        print(i)