# 2
# 5 6
# 0 0 1 0
from re import S
import sys
from itertools import *


def insert_operator():
    N = list(map(int, sys.stdin.readline().rstrip().split()))[0]
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    oper = list(map(int, sys.stdin.readline().rstrip().split()))
    oper_num = sum(oper)
    oper_arr = ["+"]*oper[0] + ["-"]*oper[1] + ["*"]*oper[2] + ["%"]*oper[3]
    oper_case = list(set(permutations(oper_arr, oper_num)))
    answer_list = list()

    for case in oper_case:
        temp_sum = arr[0]
        for i in range(len(arr)-1):
            if case[i] == "+":
                temp_sum += arr[i+1]
            elif case[i] == "-":
                temp_sum -= arr[i+1]
            elif case[i] == "*":
                temp_sum *= arr[i+1]
            else:
                if temp_sum < 0:
                    temp_sum = abs(temp_sum)
                    temp_sum //= arr[i+1]
                    temp_sum *= -1
                else:
                    temp_sum //= arr[i+1]
        answer_list.append(temp_sum)
    
    print(max(answer_list))
    print(min(answer_list))


insert_operator()