from audioop import reverse
import sys
score = dict()
for i in range(1, 9):
    score[i] = int(sys.stdin.readline())
    target = sorted(score, key=lambda x:score[x], reverse=True)[:5]
print(sum([score[i] for i in target]))
print(" ".join(map(str, sorted(target))))