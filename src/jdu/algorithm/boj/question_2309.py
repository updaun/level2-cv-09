import sys
drawf = []
for i in range(9):
    drawf.append(int(sys.stdin.readline()))
drawf = sorted(drawf)
target = sum(drawf)-100
for i in drawf:
    for j in drawf:
        if i != j:
            if target == i+j:
                for t in drawf:
                    if t != i and t != j:
                        print(t)
                exit(0)

# 조합을 활용한 다른 사람 풀이
# from itertools import combinations
# drawf = [int(input()) for _ in range(9)]
# occation = list(combinations(drawf, 7))
# print(occation)
# for i in occation:
#     if sum(i) is 100:
#         answer = list(i)
#         break
# answer.sort()
# for i in answer:
#     print(i)
