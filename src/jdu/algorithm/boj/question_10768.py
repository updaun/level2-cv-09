import sys
input = sys.stdin.readline
m = int(input())
d = int(input())
if m == 2 and d == 18:
    print('Special')
else:
    if m == 2 and d > 18:
        print('After')
    elif m >= 3:
        print('After')
    else:
        print('Before')
    