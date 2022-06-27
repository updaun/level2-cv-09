import sys
m = int(sys.stdin.readline())
answer = 1
for i in range(m):
    answer += int(sys.stdin.readline()) -1
print(answer)