import sys
n = int(sys.stdin.readline())
for i in range(n):
    p = int(sys.stdin.readline())
    players = dict()
    for _ in range(p):
        value, name = sys.stdin.readline().split()
        players[name] = int(value)
    print(sorted(players, key=lambda x:players[x], reverse=True)[0])