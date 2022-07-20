import sys
input = sys.stdin.readline
cmd_list = []
n = int(input())
for i in range(n):
    cmd_list.append(input().rstrip())
result = ''
for idx in range(len(cmd_list[0])):
    temp = cmd_list[0][idx]    
    for i in range(1, n):
        if temp != cmd_list[i][idx]:
            temp = '?'
    result += temp
print(result)
