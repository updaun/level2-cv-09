import sys
c = int(sys.stdin.readline())
n_list = []
for i in range(6):
    n_list.append(list(map(int, sys.stdin.readline().split())))
direction = [i[0] for i in n_list]
length = [i[1] for i in n_list]
max_length, sub_length = [], []

for i in range(1, 5):
    if direction.count(i) == 1:
        max_length.append(length[direction.index(i)])
        temp = direction.index(i) + 3
        if temp >= 6:
            temp -= 6
        sub_length.append(length[temp])

print((max_length[0]*max_length[1] - sub_length[0]*sub_length[1]) * c)