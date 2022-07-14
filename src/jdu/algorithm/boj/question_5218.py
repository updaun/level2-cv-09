import sys
input = sys.stdin.readline
temp = 1
alpha_dict = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    alpha_dict[i.upper()] = temp
    temp += 1
n = int(input())
for _ in range(n):
    result = 'Distances: '
    first, second = list(map(str, input().split()))
    for idx in range(len(first)):
        x = alpha_dict[first[idx]]
        y = alpha_dict[second[idx]]
        if y >= x:
            result += str(y-x) + " "
        else:
            result += str((y+26)-x) + " "
    print(result.rstrip())
