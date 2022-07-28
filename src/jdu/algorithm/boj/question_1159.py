import sys
input = sys.stdin.readline
player = {}
for i in range(int(input())):
    name = input().rstrip()[0]
    if name not in player.keys():
        player[name] = 1
    else:
        player[name] += 1
choose = []
for i in player:
    if player[i] >= 5:
        choose.append(i)
if len(choose) != 0:
    print("".join(map(str, sorted(choose))))
else:
    print("PREDAJA")