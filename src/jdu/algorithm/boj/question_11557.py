import sys
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    total = dict()
    for _ in range(k):
        name, drink = list(sys.stdin.readline().split())
        if name not in total.keys():
            total[name] = int(drink)
        else:
            total[name] += drink
    print(sorted(total, key=lambda x:total[x], reverse=True)[0])
