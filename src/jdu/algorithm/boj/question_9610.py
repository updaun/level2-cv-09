import sys
n = int(sys.stdin.readline())
space = dict()
space_list = ['Q1','Q2','Q3','Q4','AXIS']
for i in space_list:
    space[i] = 0
for i in range(n):
    x, y =  list(map(int, sys.stdin.readline().split()))
    if x == 0 or y == 0:
        space['AXIS'] += 1
    elif x > 0 and y > 0:
        space['Q1'] += 1
    elif x < 0 and y > 0:
        space['Q2'] += 1
    elif x < 0 and y < 0:
        space['Q3'] += 1
    else:
        space['Q4'] += 1
for i in space_list:
    print(f"{i}: {str(space[i])}")
