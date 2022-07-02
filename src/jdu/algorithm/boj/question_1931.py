import sys
n = int(sys.stdin.readline())
schedules = []
for i in range(n):
    schedules.append(list(map(int, sys.stdin.readline().split())))
result = []
meetings = sorted(schedules, key=lambda x:(x[0], x[1]))
for i in range(int(len(meetings)/2)):
    count = 0
    start = 0
    temp = meetings[i:]
    for idx in range(len(temp)):
        meet = temp[idx]
        if start <= meet[0]:
            count += 1
            start = meet[1]
    result.append(count)
print(max(result))