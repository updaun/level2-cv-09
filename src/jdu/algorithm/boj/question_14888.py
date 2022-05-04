import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
oper_list = list(map(int, sys.stdin.readline().split()))

min_cal = 1e9
max_cal = min_cal * -1

def backtracking(result, count):
    global min_cal, max_cal
    if count ==  n-1:
        if min_cal > result:
            min_cal = result
        if max_cal < result:
            max_cal = result
        return
    
    for i in range(4):
        if oper_list[i] != 0:
            oper_list[i] -= 1
            if i == 0:
                backtracking(result + n_list[count+1], count+1)
            elif i == 1:
                backtracking(result - n_list[count+1], count+1)
            elif i == 2:
                backtracking(result * n_list[count+1], count+1)
            elif i == 3:
                backtracking(int(result / n_list[count+1]), count+1)
            oper_list[i] += 1

backtracking(n_list[0], 0)

print(int(max_cal))
print(int(min_cal))