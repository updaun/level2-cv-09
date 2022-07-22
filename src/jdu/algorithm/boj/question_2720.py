import sys
input = sys.stdin.readline
n = int(input())
coins = [25, 10, 5, 1]
for i in range(n):
    coins_count = [0, 0, 0, 0]
    target = int(input())
    for idx in range(4):
        if target >= coins[idx]:
            count, change = divmod(target, coins[idx])
            coins_count[idx] += count
            target = change
    print(" ".join(map(str, coins_count)))