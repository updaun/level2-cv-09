import sys
N,M = list(map(int, sys.stdin.readline().split()))
n_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0]

# 시간 초과
# for _ in range(M):
#     i,j = list(map(int, sys.stdin.readline().split()))
#     print(sum(n_list[i:j+1]))

temp = 0
for i in n_list:
    temp += i
    sum_list.append(temp)

for i in range(M):
    i,j = list(map(int, sys.stdin.readline().split()))
    print(sum_list[j]-sum_list[i-1])
