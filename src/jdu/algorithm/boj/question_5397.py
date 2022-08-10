import sys
input = sys.stdin.readline
for _ in range(int(input())):
    log = input().rstrip()
    left, right = [], []
    for i in log:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    answer = left + right[::-1]
    print("".join(answer))
    


# 시간 초과
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     log = input().rstrip()
#     idx = 0
#     pwd = []
#     for i in log:
#         if idx < 0:
#             idx = 0
#         if idx > len(pwd):
#             idx = len(pwd)
#         if i == '<':
#             idx -= 1
#         elif i == '>':
#             idx += 1
#         elif i == '-':
#             if len(pwd) != 0:
#                 pwd.pop(idx-1)
#                 idx -= 1
#         else:
#             pwd.insert(idx, i)
#             idx += 1
#     print("".join(map(str, pwd)))