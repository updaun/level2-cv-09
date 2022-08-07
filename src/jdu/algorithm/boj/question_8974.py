A, B = map(int, input().split())
num_list = []
temp = 0
for i in range(1, 50):
    for j in range(1, i+1):
        temp += i
        num_list.append(temp)
if A == 1:
    print(num_list[B-1])
else: 
    print(num_list[B-1]-num_list[A-2])