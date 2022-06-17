import sys
bowl = sys.stdin.readline().strip()
length = 10
start = bowl[0]
for i in range(1, len(bowl)):
    if bowl[i] == start:
        length += 5
    else:
        length += 10
    start = bowl[i]
print(length)