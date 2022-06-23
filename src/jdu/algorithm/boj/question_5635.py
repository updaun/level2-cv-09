import sys
n = int(sys.stdin.readline())
people = dict()
for i in range(n):
    name, dd, mm, yyyy = sys.stdin.readline().split()
    people[name] = [int(dd), int(mm), int(yyyy)]
target = sorted(people, key=lambda x:(people[x][2], people[x][1], people[x][0]))
print(target[-1])
print(target[0])