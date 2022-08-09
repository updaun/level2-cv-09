import sys
input = sys.stdin.readline
for _ in range(int(input())):
    coin = input().rstrip()
    c_list = [0] * 8
    for i in range(len(coin)-2):
        temp = 0
        target = coin[i:i+3][::-1]
        for t in range(3):
            if target[t] == 'H':
                temp += 2**t
        c_list[temp] += 1
    print(" ".join(map(str, c_list)))
