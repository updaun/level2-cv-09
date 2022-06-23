import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
num = M
sqrt_num = 1
answer = []
while N >= num:
    if num == sqrt_num**2:
        answer.append(num)
        num += 1
    else:
        if num > sqrt_num**2:
            sqrt_num += 1
        else:
            num = sqrt_num**2
if len(answer) == 0:
    print(-1)          
else:
    print(sum(answer))
    print(answer[0])    