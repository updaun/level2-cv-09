import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
part_list = sorted(list(map(int, input().split())))
count = 0
for i in range(N):
    if M-part_list[i] in part_list:
        count += 1
print(int(count/2))
