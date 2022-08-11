import sys
input = sys.stdin.readline
game = [0, 1, 0, 0]
for i in range(int(input())):
    a, b = map(int, input().split())
    temp_a, temp_b = game[a], game[b]
    game[a] = temp_b
    game[b] = temp_a
print(game.index(1))