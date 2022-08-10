import sys
input = sys.stdin.readline
for i in range(int(input())):
    s = 0
    ps = input().rstrip()
    for p in ps:
        if p == '(':
            s += 1
        else:
            s -= 1
            if s < 0:
                break
    if s == 0:
        print("YES")
    else:
        print("NO")