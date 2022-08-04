import sys
input = sys.stdin.readline
answer = [int((i-1)%5 + 1) for i in range(1, 11)]
score = []
for _ in range(int(input())):
    t = list(map(int, input().split()))
    score.append(sum([int(answer[i]==t[i]) for i in range(10)]))
for i in range(len(score)):
    if score[i] == 10:
        print(i+1)