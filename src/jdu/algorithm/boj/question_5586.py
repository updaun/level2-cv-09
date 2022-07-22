import sys
target = sys.stdin.readline().rstrip()
i_count = 0
j_count = 0
for i in range(len(target)):
    if target[i:i+3] == 'IOI':
        i_count += 1
    elif target[i:i+3] == 'JOI':
        j_count += 1
print(j_count)
print(i_count)
