import sys
input = sys.stdin.readline
n = int(input())
num_list = []
triger = True
for i in range(n):
    num_list.append(int(input()))
if num_list[2]-num_list[1] == num_list[1]-num_list[0]:
    triger = False
if triger:
    print(int(num_list[-1]*num_list[1]/num_list[0]))
else:
    print(num_list[-1]+(num_list[1]-num_list[0]))
